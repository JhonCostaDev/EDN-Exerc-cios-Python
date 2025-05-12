import streamlit as st
import google.generativeai as genai
import os

# Configurar a API
genai.configure(api_key='apiKey')

# Inicializar o modelo
model = genai.GenerativeModel("gemini-1.5-flash")
st.image("https://media.licdn.com/dms/image/v2/D4E22AQF80K8NOo5GPw/feedshare-shrink_2048_1536/B4EZYWByQ6HkAo-/0/1744126290443?e=1749686400&v=beta&t=tWwNy1Cj5oRgNj6b0NGp0oLtAYBqhmRUKp62WyQq-IQ", width=600)

st.title("Blue Guardian")

st.markdown("<h1 style='text-align: center;'>Monitorando hoje para preservar o amanhã</h1>", unsafe_allow_html=True)

# Criando um campo de entrada de chat
mensagem = st.chat_input("Digite sua mensagem...")

if mensagem:
    response = model.generate_content(mensagem)
    st.chat_message("user").write(mensagem)
    st.chat_message("assistant").write(response.text)
