import streamlit as st
import input 
import output 
import re

st.set_page_config(page_title="Suspicious Chat Detector", page_icon=":guardsman:", layout="wide")
st.title("Suspicious Chat Detector")
st.markdown(
    """
    **Upload a chat log to check if it contains any suspicious messages.**
    
    This app helps detect suspicious or illegal content in chat logs by analyzing messages based on pre-trained models.
    """
)

st.sidebar.header("Upload Chat Log")
file = st.sidebar.file_uploader("Upload a chat file", type="txt")

def is_valid_whatsapp_chat(chat_lines):
    whatsapp_pattern = r'^\[[^\]]+\]\s+[^\:]+: *'
    for line in chat_lines:
        if re.match(whatsapp_pattern, line):
            return True 
    return False

def process_chat(file):
    chat_lines = file.read().decode("utf-8").splitlines()
    if not is_valid_whatsapp_chat(chat_lines):
        st.error("The uploaded file is not a valid WhatsApp chat exported from iOS.")
        return None
    cleaned_chat = input.extract_text_messages(chat_lines)
    st.write("### Cleaned Chat Messages:")
    for msg in cleaned_chat[:5]:
        st.write(msg)
    is_illegal = output.check_illegal_chat(cleaned_chat, output.model, output.vectorizer, threshold=0.2)
    return is_illegal

if file is not None:
    st.sidebar.subheader("File Information")
    st.sidebar.write(f"**File Name**: {file.name}")
    st.sidebar.write(f"**File Size**: {file.size} bytes")
    
    progress_bar = st.progress(0)

    is_illegal = None
    with st.spinner("Processing the chat..."):
        for percent_complete in range(100):
            progress_bar.progress(percent_complete + 1)
        is_illegal = process_chat(file)
    
    if is_illegal is not None: 
        if is_illegal:
            st.markdown("<h2 style='color:red;'>The chat is classified as **Illegal**.</h2>", unsafe_allow_html=True)
        else:
            st.markdown("<h2 style='color:green;'>The chat is classified as **Legal**.</h2>", unsafe_allow_html=True)
else:
    st.info("Please upload a `.txt` file to analyze.")

 
    





