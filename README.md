# Sentiment Analysis Dashboard

A web application designed to perform real-time sentiment analysis and compare rule-based and deep-learning approaches.

# Features

## Dual-model comparison
Sentiment analysis is performed using both TextBlob (rule-based) and a HuggingFace Transformers model (DistilBERT), allowing direct comparison of results from linguistic rules and contextual deep learning.

## Batch dataset processing
CSV files can be uploaded to run sentiment analysis on large datasets, with automated charts generated to visualize overall trends and results.

## Optimized performance
Model loading is cached using Streamlit to reduce startup time and improve overall responsiveness.

# Tech Stack
Frontend: Streamlit

Machine Learning: PyTorch, HuggingFace Transformers (DistilBERT), TextBlob

Data Analysis & Visualization: Pandas, Plotly

Environment: Python 3.12 virtual environment (venv)
## Setup Instructions

1. Clone the repository

        git clone https://github.com/cayla-hhh/Sentiment-Analysis-Web-App.git
        cd sentiment-analysis-app

2. Create and activate a virtual environment

        python -m venv .venv

       .\.venv\Scripts\activate

4. Install dependencies

        pip install -r requirements.txt

4. Run the application

        streamlit run app.py
