import streamlit as st
from langchain_ollama import ChatOllama
import base64
from langchain_core.messages import HumanMessage

llm = ChatOllama(
    model="gemma4:latest"
)

st.title("AI图生文系统")

uploaded_file = st.file_uploader("上传图片")
if uploaded_file is not None:
    with st.chat_message("human"):
        st.image(uploaded_file)

    bytes_data=uploaded_file.getvalue()
    base64_str=base64.b64encode(bytes_data).decode("utf-8")

    message = HumanMessage(
        content=[
            {"type":"text","text":"请描述这张图片的内容"},
            {
        "type": "image_url",
        "image_url": {"url": f"data:{uploaded_file.type};base64,{base64_str}"}
        },
        ]
    )

    with st.chat_message("ai"):
        ai_reply=llm.invoke([message])
        st.write(ai_reply.content)