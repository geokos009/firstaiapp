from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import LLMChain
from langchain import PromptTemplate

import os

os.environ['GOOGLE_API_KEY'] = "AIzaSyCBvxOuY0GQYlCD74aVGIdOzokMpkllfMs"

# Create prompt template for generating facebook posts

fb_template = "GIve me {number} of fb posts on {topic}"

fb_prompt = PromptTemplate(template = fb_template, input = ['number', 'topic'])

# Initialize Google's Gemini AI model

gemini_model = ChatGoogleGenerativeAI(model = "gemini-1.5-flash-latest")

# Create LLM chain byusing the prompt template and model

fbpost_chain = fb_prompt | gemini_model

# Example of using the LLM chain

response = fbpost_chain.invoke({"number" : 5, "topic" : "Wars in Middle East"})