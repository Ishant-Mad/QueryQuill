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

def process_run(st, thread_id, assistant_id):
    st.session_state.last_message = None
    response = runAssistant(thread_id, assistant_id)
    thread_messages = response["response"]

    for message in thread_messages:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if message['role'] == 'user':
            with st.container():
                st.markdown(
                    f"""
                    <div class="chat-container">
                        <div class="chat-header">
                            <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Grinning%20Cat%20with%20Smiling%20Eyes.png" alt="User">
                            <span>You</span>
                        </div>
                        <div class="chat-message user">
                            {message['content']}
                        </div>
                        <div class="chat-timestamp">{timestamp}</div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            with st.container():
                st.markdown(
                    f"""
                    <div class="chat-container">
                        <div class="chat-header">
                            <img src="https://raw.githubusercontent.com/Tarikul-Islam-Anik/Animated-Fluent-Emojis/master/Emojis/Smilies/Robot.png" alt="Assistant">
                            <span>Assistant</span>
                        </div>
                        <div class="chat-message assistant">
                            {message['content']}
                        </div>
                        <div class="chat-timestamp">{timestamp}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
def main():
    st.markdown("""
    <div class="title">InsightAI Suite</div>
    <div class="description">
        Revolutionize how you find and use information with intelligent search and comprehensive content analysis.<br><br>
        Empower your data with advanced analytics and search technology.<br><br>
    </div>
    """, unsafe_allow_html=True)

    if 'assistant_initialized' not in st.session_state:
        title = st.text_input("Enter the title", key="title")
        initiation = st.text_input("Enter the assistant's first question", key="initiation")
        uploaded_files = st.file_uploader("Upload Files for the Assistant", accept_multiple_files=True, key="uploader")
        file_locations = []

        if uploaded_files and title and initiation:
            for uploaded_file in uploaded_files:
                bytes_data = uploaded_file.getvalue()
                location = f"temp_file_{uploaded_file.name}"
                with open(location, "wb") as f:
                    f.write(bytes_data)
                file_locations.append(location)
                st.success(f'✅ File {uploaded_file.name} has been uploaded successfully.')

            with st.spinner('Processing your file and setting up the assistant...'):
                file_ids = [saveFileOpenAI(location) for location in file_locations]
                assistant_id, vector_id = createAssistant(file_ids, title)
                thread_id = startAssistantThread(initiation, vector_id)

            st.session_state.thread_id = thread_id
            st.session_state.assistant_id = assistant_id
            st.session_state.last_message = initiation
            st.session_state.assistant_initialized = True

            process_run(st, thread_id, assistant_id)

    if 'assistant_initialized' in st.session_state and st.session_state.assistant_initialized:
        follow_up = st.text_input("Enter your follow-up question", key="follow_up")
        submit_button = st.button("Submit Follow-up")

        if submit_button and follow_up and follow_up != st.session_state.last_message:
            st.session_state.last_message = follow_up
            addMessageToThread(st.session_state.thread_id, follow_up)
            process_run(st, st.session_state.thread_id, st.session_state.assistant_id)

if __name__ == "__main__":
    main()