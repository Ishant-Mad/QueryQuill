import streamlit as st
from assistants import *
import time
from datetime import datetime

# Custom CSS for chat style and updated title/description
st.markdown("""
<style>
    .chat-container {
        display: flex;
        flex-direction: column;
        align-items: flex-start;
        margin-bottom: 10px;
    }
    .chat-message {
        max-width: 70%;
        padding: 10px;
        margin: 10px 0;
        border-radius: 10px;
        font-size: 16px;
        color: #fff;
    }
    .chat-message.user {
        background-color: #007ACC;
        align-self: flex-end;
        border-top-right-radius: 0;
    }
    .chat-message.assistant {
        background-color: #282C34;
        border-top-left-radius: 0;
    }
    .chat-header {
        display: flex;
        align-items: center;
        margin-bottom: 5px;
    }
    .chat-header img {
        border-radius: 50%;
        width: 30px;
        height: 30px;
        margin-right: 10px;
    }
    .chat-timestamp {
        font-size: 12px;
        color: #999;
        margin-top: 5px;
    }
    .title {
        font-family: 'Arial', sans-serif;
        font-size: 36px;
        font-weight: bold;
        color: #00BFFF; /* Light Sky Blue */
        text-align: center;
        margin-top: 20px;
    }
    .description {
        font-family: 'Arial', sans-serif;
        font-size: 18px;
        color: #E0E0E0; /* Light Grey */
        text-align: center;
        margin: 10px auto;
        width: 80%;
    }
    .emoji {
        font-size: 20px; /* Smaller size for a more professional look */
    }
</style>
""", unsafe_allow_html=True)