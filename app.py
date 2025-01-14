# Q&A Chatbot
from langchain.llms import OpenAI
from langchain_openai import ChatOpenAI 
from dotenv import load_dotenv
load_dotenv()  # take environment variables from .env.

import streamlit as st
import os


## Function to load OpenAI model and get respones
def get_openai_response(question):
    llm = ChatOpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name="gpt-4o-2024-08-06",temperature=0.5)
    response = llm.invoke(question)

    # Check if the response is an object and extract content properly
    if hasattr(response, "content"):
        return response.content  # Extract response text correctly

    return response  # Fallback to returning the raw response

## initialize our streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Langchain Chatbot")

input = st.text_input("Enter your question: ",key="input")

submit = st.button("Ask...")

## If ask button is clicked
if submit:
    response = get_openai_response(input)
    st.subheader("The Response is:")
    st.write(response)




