#TODO: Install before running
#pip install gradio
#pip install google.generativeai
#pip install gradio_pdf

#run code - python gemini-chat-app.py

import gradio as gr
import os
import google.generativeai as genai


#custom theme
theme = gr.themes.Base(
    secondary_hue="gray",
).set(
    border_color_accent_dark='*neutral_800'
)


def gemini_chat(message, history,content_type,content_objective,acceptance_criteria,image):
    #response = chat.send_message(message)
    #TODO: Make conditional the additional inputs and the image
    response = model.generate_content("Generate content where the theme is "+message+" the content type is meant to be used in a "+content_type+". The content objective is "+content_objective+". The acceptance criteria for the generated content is "+acceptance_criteria,image)
    return response.text

API_KEY = os.getenv('GOOGLE_API_KEY') 
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

iface = gr.ChatInterface(
    fn=gemini_chat, 
    title='IE GenExperience',
    additional_inputs_accordion = gr.Accordion(label="Additional Parameters", open=True),
    chatbot=gr.Chatbot(),
    textbox=gr.Textbox(
        placeholder="Theme...",
        scale=7
    ),
    #retry_btn=None,
    undo_btn=None,
    clear_btn=None,
    theme=theme,
     additional_inputs= [
        gr.Dropdown(["Forum", "Lecture", "Exercises"], label="Content Type"),
        gr.Textbox(label="Content Objective"),
        gr.Textbox(label="Acceptance Criteria")
        ]
   
)

if __name__ == '__main__':
    iface.launch(share=True)