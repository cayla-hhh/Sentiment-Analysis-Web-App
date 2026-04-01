import streamlit as st
from textblob import TextBlob


st.title("Sentiment Analysis Dashboard")

user_text = st.text_input("Enter some text to analyze:")

if user_text:
    blob = TextBlob(user_text)
    score = blob.sentiment.polarity

    if score > 0:
        label = "Positive"
    elif score < 0:
        label = "Negative"
    else:
        label = "Neutral"

st.subheader(f"Sentiment: {label}")
st.write(f"Confidence Score: {score}")