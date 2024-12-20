# pip install streamlit
# pip install langchain
# pip install langchain-google-genai
# pip install streamlit

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import os

os.environ['Google_API_KEY'] = "AIzaSyADi4EDeVNnjv5yoqpiOwmy8rw0qpbfS9M"

# Create prompt template for generating tweets

tweet_template = "Give me {number} tweets about {topic}"

tweet_prompt = PromptTemplate(template = tweet_template, input_variables = ["number", "topic"])

#Initializing Google's Gemini model

gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

#Creating the LLMChain object using the prompt template and the model

tweet_chain = tweet_prompt | gemini_model

#Example usage of LLMChain object

response = tweet_chain.invoke({"number": 1, "topic": "AI"})
 
import streamlit as st

st.header("Tweet Generator")

st.subheader("Enter the text you want to generate the tweet for")
topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1, step=1)

if st.button("Generate Tweet"): 
    tweets = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweets.content)
