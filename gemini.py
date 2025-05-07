import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from io import BytesIO
from fpdf import FPDF

# App Title
st.title("🧠 Gemini AI Playground")

# API Key Input
api_key = st.text_input("Enter your Gemini API Key", type="password")
if api_key:
    os.environ["GEMINI_API_KEY"] = api_key
    genai.configure(api_key=api_key)

    # Model selection
    model_name = st.selectbox("Choose a Gemini Model", [
        'gemini-2.5-flash-preview-04-17',
        'gemini-2.5-pro-exp-03-23',
        'gemini-1.5-flash',
        'models/text-embedding-004'
    ])
    
    model = genai.GenerativeModel(model_name)

    # Tabs
    tab = st.sidebar.radio("Choose Action", ["Text Generation", "Image + Prompt", "Embedding", "Token Count", "PDF Generator"])

    # --- TEXT GENERATION ---
    if tab == "Text Generation":
        prompt = st.text_area("Enter your prompt")
        if st.button("Generate"):
            response = model.generate_content(prompt)
            st.markdown(response.text)

    # --- IMAGE + PROMPT ---
    elif tab == "Image + Prompt":
        prompt =
