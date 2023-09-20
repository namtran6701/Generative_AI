# Generative AI
 Generative AI application
- In this repo, I created three AI models with a user-friendly local interface (gradio) that allows users to interact with the AI model.
1. Image processing (Image to text)
- In this model, I use blip image captioning base API developed by Salesforce to generate captions from images
- Users can upload the image, and the algorithm will analyze the image and produce the corresponding caption
- Code for the model can be found under Image_Processing.ipynb

2. Image generation (Text to image)
- In this model, we attempt to generate image form a text description using a stable diffusion model
- The LLM used is runwayml/stable-diffusion-v1-5
- Code for the file can be found under Image_Generation.ipynb

3. Describe and Generate Image
- In this model, we will allow user to upload their image, then the algorithm will analyze the image, generate the corresponding question, finally generate an image from that caption. 
