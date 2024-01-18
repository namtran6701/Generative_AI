# Import needed libraries 
import os
import io
import accelerate
import IPython.display
from PIL import Image
import base64
from dotenv import load_dotenv, find_dotenv
from diffusers import StableDiffusionPipeline
import torch
import requests, json
import gradio as gr
from transformers import pipeline
from random import randint
from diffusers import DiffusionPipeline
_ = load_dotenv(find_dotenv()) # read local .env file
os.environ['HF_API_KEY'] = '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'
hf_api_key = os.environ['HF_API_KEY']


# 1. Image to text generation pipeline
itt_pipe = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning")
## Create a fucntion to obtain the caption only
captioner = lambda x: itt_pipe(x)[0]['generated_text']

# 2. text to image generation pipeline 
tti_pipe = DiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16)
tti_pipe = tti_pipe.to("cuda")
generate = lambda x:tti_pipe(x).images[0]

# 3. Combine the two pipelines
def caption_and_generate(selected_image, uploaded_image):
    if uploaded_image is None:
        return "Please upload an image."

    caption = captioner(uploaded_image)
    generated_image = generate(caption)
    return [caption, generated_image]


port_number = randint(1000,9999)

os.environ['PORT3'] = str(port_number)


with gr.Blocks() as demo:
    gr.Markdown('Describe and Generate Image')

    with gr.Row():
        with gr.Column():
            image_selection = gr.Dropdown(label='Select a Sample Image', choices=list(sample_images.keys()))
            image_upload = gr.Image(label='Or upload your image', type='pil')
        with gr.Column():
            btn_all = gr.Button('Caption and Generate')
    caption = gr.Textbox(label='Generated Caption')
    image_output = gr.Image(label='Generated Image')

    btn_all.click(fn=caption_and_generate, inputs=[image_selection, image_upload], outputs=[caption, image_output])

gr.close_all()
demo.launch(share=False, server_port=int(os.environ['PORT3']))