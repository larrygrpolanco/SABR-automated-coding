import streamlit as st
import pandas as pd
import time
from chatgpt_coder import ChatGPTCoder

# Initialize the ChatGPTCoder with your OpenAI API key
gpt_coder = ChatGPTCoder(st.secrets["OPENAI_API_KEY"])


st.title("Auto SABR Coding")
st.markdown("Prototype app for testing automatic SABR coding using LLMs.")