import streamlit as st
import google.generativeai as genai
import os

# ================================ Gemini
genai.configure(api_key='AIzaSyCOUzxGXgtXARw4iWLx7V2l6swnF15fXCI')

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Olá, como posso ajudar?")
#print(response.text)

st.image("https://media.licdn.com/dms/image/v2/D4E22AQF80K8NOo5GPw/feedshare-shrink_2048_1536/B4EZYWByQ6HkAo-/0/1744126290443?e=1749686400&v=beta&t=tWwNy1Cj5oRgNj6b0NGp0oLtAYBqhmRUKp62WyQq-IQ", width=600)

# ================================ Gemini

# ================================ Streamlit
st.markdown("<h1 style='text-align: center;'>Monitorando hoje para preservar o amanhã</h1>", unsafe_allow_html=True)



# Entrada

#while True:
message = st.chat_input("Digite sua pergunta...")
#if message == 'sair':
 #   break
response = model.generate_content(message)
if message:
    st.write(f'Você digitou: {response}')