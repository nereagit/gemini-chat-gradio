import gradio as gr
import os
import google.generativeai as genai

def gemini_chat(message, history):
    response = chat.send_message(message)
    return response.text

css = """
#text {
  position: absolute;
  bottom: 0;
  width: 100%;
}
"""

API_KEY = os.getenv('GOOGLE_API_KEY')

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat()

iface = gr.ChatInterface(
    fn=gemini_chat, 
    title='Gemini Chat',
    chatbot=gr.Chatbot(height='100%')
)

if __name__ == '__main__':
    iface.launch()