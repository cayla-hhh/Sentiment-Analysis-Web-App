import streamlit as st
from textblob import TextBlob

# Sidebar
st.sidebar.header("Dashboard Controls")

model_choice = st.sidebar.selectbox("Choose Analysis Engine:", ["TextBlob (Fast)", "HuggingFace (Advanced)"])

uploaded_file = st.sidebar.file_uploader("Batch Process CSV", type=["csv"])

# Main Content
st.title("AI Sentiment Dashboard")

user_text = st.text_area("Analyze specific text:", placeholder="Enter a sentence here...")

if user_text:
    blob = TextBlob(user_text)

    pol = blob.sentiment.polarity
    subj = blob.sentiment.subjectivity

    col1, col2, col3 = st.columns([2, 1, 1])
