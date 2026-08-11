import streamlit as st
from langchain_ollama import ChatOllama

st.set_page_config(page_title="AI实时问答系统", page_icon="🤖", layout="wide")

llm = ChatOllama(
    model="gemma4:latest"
)

st.title("AI实时问答系统")
prompt=st.chat_input("请输入您的问题...")

if prompt:
    user_message=st.chat_message("user")
    user_message.write(prompt)

    ai_message=st.chat_message("ai")
    ai_reply=llm.invoke(prompt)
    ai_message.write(ai_reply.content)