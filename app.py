import google.generativeai as genai

import streamlit as st

file_path = "C:\code_reviewer\generative.txt"
with open(file_path, mode='r') as key:
    api = key.read()

genai.configure(api_key=api)
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", system_instruction='you are chat bot which provides data science related content')

st.title('Ai tutor')

st.chat_message('assistant').write('Good Day! welcome to AI Tutor..Feel free to post your Doubts')

if 'memory' not in st.session_state:
    st.session_state['memory'] = []
chat = model.start_chat(history=st.session_state['memory'])

for msg in st.session_state['memory']:
    st.chat_message('user').write(msg, role='user')
user_input = st.chat_input()

if user_input:
    #st.session_state['memory'].append(user_input)
    st.chat_message('user').write(user_input, role='user')
    chat_response = chat.send_message(user_input)
    st.chat_message('ai').write(chat_response.text, role='model')



															   																					   