# AI Sentiment Analysis Dashboard
A high-performance web application that performs real-time sentiment analysis using both rule-based and deep-learning AI models.

##  Key Features
* **Dual-Engine Analysis:** Compare results between **TextBlob** (Linguistic rules) and **HuggingFace Transformers** (Contextual Deep Learning).
* **Batch Processing:** Upload CSV files for large-scale data analysis with automated visualization.
* **Resource Caching:** Utilizes Streamlit's `@st.cache_resource` for optimized model loading.

##  Technical Stack
* **Frontend:** Streamlit 
* **Machine Learning:** PyTorch, Transformers (DistilBERT), TextBlob 
* **Data Science:** Pandas, Plotly 
* **Environment:** Python 3.12 Virtual Environment (venv) 

## Quick Start

### 1. Clone the Repository
    git clone https://github.com/cayla-hhh/Sentiment-Analysis-Web-App.git
    cd sentiment-analysis-app

### 2. Set Up the Environment
### Create and activate the virtual environment
    python -m venv .venv

    .\.venv\Scripts\activate

### 3. Install Dependencies
    pip install -r requirements.txt

### 4. Run the App
    streamlit run app.py
