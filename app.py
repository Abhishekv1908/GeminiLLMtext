from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("Google_API_Key"))

# Function to load Gemini Pro model and get responses
model = genai.GenerativeModel("gemini-2.0-flash")

def get_gemini_response(question):
    response = model.generate_content(question)  # Assign the response
    return response.text  # Return the actual text

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo By Abhishek")
st.header("Gemini LLM Application By Abhishek")

# Input field
user_input = st.text_input("Input", key="input")
submit = st.button("Ask the question")

# When submit is clicked
if submit:
    response = get_gemini_response(user_input)
    st.subheader("The response is:")
    st.write(response)

    