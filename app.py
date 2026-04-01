import streamlit as st
from textblob import TextBlob
import plotly.graph_objects as go
import pandas as pd
from transformers import pipeline

@st.cache_resource
def load_hf_pipeline():
    return pipeline("sentiment-analysis")

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
        classifier = load_hf_pipeline()
        result = classifier(user_text)[0]

        if result['label'] == 'POSITIVE':
            pol = result['score']
        else:
            pol = -result['score']
        
        subj = 0.5

    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.metric("Polarity Score", f"{pol:.2f}")
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

if uploaded_file is not None:
    st.divider()
    st.header('Batch Analysis Mode')

    df = pd.read_csv(uploaded_file)

    column_to_analyze = st.selectbox("Select the column containing text:", df.columns)

    if st.button("Run Batch Analysis"):
        df['Polarity'] = df[column_to_analyze].apply(lambda x: TextBlob(str(x)).sentiment.polarity)

        avg_polarity = df['Polarity'].mean()
        st.metric("Average Batch Sentiment", f"{avg_polarity:.2f}")

        st.dataframe(df)