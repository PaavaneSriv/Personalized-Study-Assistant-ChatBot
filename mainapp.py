# MAIN.py --- run SUCCESSFUL

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import fitz  # PyMuPDF

# Load .env file
load_dotenv()

# Configure Gemini API key
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Initialize model
model = genai.GenerativeModel("models/gemini-2.0-flash")

# Session state init
if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_text" not in st.session_state:
    st.session_state.pdf_text = ""

# Sidebar
with st.sidebar:
    st.header("Upload PDF")
    pdf_file = st.file_uploader("Upload Study Material (PDF)", type=['pdf'])
    if pdf_file is not None:
        pdf_reader = fitz.open(stream=pdf_file.read(), filetype="pdf")
        text = ""
        for page in pdf_reader:
            text += page.get_text()
        st.session_state.pdf_text = text
        st.success("PDF loaded! You can now ask questions from it.")

    # Clear chat button
    if st.button("🗑️ Clear Chat History"):
        st.session_state.messages = []
        st.session_state.tokens_used = 0
        st.success("Chat history cleared!")

# Main Title
st.title("📚 Personal Study Assistant Chatbot")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask your question here..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Build chat prompt with PDF content (optional) + chat history
    history_text = ""
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            history_text += f"\nUser: {msg['content']}\n"
        else:
            history_text += f"\nAssistant: {msg['content']}\n"

    full_prompt = f"""
    You are a helpful study assistant.
    The user has provided this optional study material:

    {st.session_state.pdf_text[:4000]}

    Conversation history:
    {history_text}

    Now answer the latest question:
    {prompt}
    """

    # Get Gemini response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.generate_content(full_prompt)
            response_text = response.text
            st.markdown(response_text)

    # Add assistant message to history
    st.session_state.messages.append({"role": "assistant", "content": response_text})