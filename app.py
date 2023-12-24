from dotenv import load_dotenv

load_dotenv()  

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("google_api_key"))

## Function to load OpenAI
model=genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

##initialize streamlit

st.set_page_config(page_title="Question and Answer Demo")

st.header("Gemini Application")

input=st.text_input("Input: ",key="input")


submit=st.button("Ask the question")


if submit:
    
    response=get_gemini_response(input)
    st.subheader("Response")
    st.write(response)