import streamlit as st
from textblob import TextBlob
import plotly.graph_objects as go

# Sidebar
st.sidebar.header("Dashboard Controls")

model_choice = st.sidebar.selectbox("Choose Analysis Engine:", ["TextBlob (Fast)", "HuggingFace (Advanced)"])

uploaded_file = st.sidebar.file_uploader("Batch Process CSV", type=["csv"])

# Main Content
st.title("AI Sentiment Dashboard")

user_text = st.text_area("Analyze specific text:", placeholder="Enter a sentence here...")

if user_text:
    if model_choice == "TextBlob (Fast)":
        blob = TextBlob(user_text)
        pol = blob.sentiment.polarity
        subj = blob.sentiment.subjectivity
    else:
        # Placeholder
        pol = 0.5
        subj = 0.5
        st.warning("HuggingFace model coming soon")

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.metric("Polarity Score" f"{pol:.2f}")
    with col2:
        st.metric("Subjectivity", f"{subj:.2f}")

    with col3:
        if pol > 0:
            label = "Positive"
        elif pol < 0:
            label = "Negative"
        else:
            label = "Neutral"
        st.write(f"**Result:**{label}")
    st.divider()
    # Gauge
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = pol,
        title = {'text': "Sentiment Visualizer"},
        gauge = {'axis': {'range': [-1, 1]}}
    ))

    st.plotly_chart(fig, use_container_width=True)
