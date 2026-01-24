"""
Sentiment Analysis Web Application
A real-time sentiment analyzer using transformer models
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from transformers import pipeline
import torch
from datetime import datetime
import time

# Page configuration
st.set_page_config(
    page_title="Sentiment Analysis Dashboard",
    page_icon="🎭",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stAlert {
        margin-top: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)


@st.cache_resource
def load_model():
    """
    Load the sentiment analysis model with caching
    Uses distilbert-base-uncased-finetuned-sst-2-english
    """
    try:
        # Check if CUDA is available
        device = 0 if torch.cuda.is_available() else -1
        
        # Load the sentiment analysis pipeline
        sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device=device
        )
        return sentiment_pipeline
    except Exception as e:
        st.error(f"Error loading model: {str(e)}")
        return None


def analyze_sentiment(text, model):
    """
    Analyze sentiment of given text
    
    Args:
        text: Input text to analyze
        model: Loaded sentiment pipeline
    
    Returns:
        dict: Sentiment result with label and score
    """
    try:
        # Truncate text if too long (model max is 512 tokens)
        if len(text.split()) > 400:
            text = ' '.join(text.split()[:400])
        
        result = model(text)[0]
        return result
    except Exception as e:
        st.error(f"Error analyzing sentiment: {str(e)}")
        return None


def create_sentiment_gauge(score, label):
    """
    Create a gauge chart for sentiment visualization
    
    Args:
        score: Confidence score
        label: Sentiment label (POSITIVE/NEGATIVE)
    """
    # Adjust score based on label
    if label == "NEGATIVE":
        display_score = (1 - score) * 50  # 0-50 range for negative
    else:
        display_score = 50 + (score * 50)  # 50-100 range for positive
    
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=display_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Sentiment Score", 'font': {'size': 24}},
        delta={'reference': 50, 'increasing': {'color': "green"}, 'decreasing': {'color': "red"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkblue"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 33], 'color': '#ffcccc'},
                {'range': [33, 66], 'color': '#ffffcc'},
                {'range': [66, 100], 'color': '#ccffcc'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50
            }
        }
    ))
    
    fig.update_layout(height=300, margin=dict(l=20, r=20, t=50, b=20))
    return fig


def main():
    # Header
    st.title("🎭 Sentiment Analysis Dashboard")
    st.markdown("""
    Analyze the sentiment of any text using state-of-the-art AI! 
    This app uses a fine-tuned DistilBERT model to detect positive or negative sentiment.
    """)
    
    # Sidebar
    with st.sidebar:
        st.header("ℹ️ About")
        st.info("""
        **How it works:**
        1. Enter your text in the input box
        2. Click 'Analyze Sentiment'
        3. View results and confidence scores
        
        **Model:** DistilBERT fine-tuned on SST-2
        
        **Capabilities:**
        - Real-time sentiment detection
        - Confidence scoring
        - Batch analysis
        """)
        
        st.header("📊 Statistics")
        if 'history' not in st.session_state:
            st.session_state.history = []
        
        if len(st.session_state.history) > 0:
            df_history = pd.DataFrame(st.session_state.history)
            positive_count = len(df_history[df_history['label'] == 'POSITIVE'])
            negative_count = len(df_history[df_history['label'] == 'NEGATIVE'])
            
            st.metric("Total Analyses", len(st.session_state.history))
            st.metric("Positive", positive_count)
            st.metric("Negative", negative_count)
    
    # Load model
    with st.spinner("Loading AI model..."):
        model = load_model()
    
    if model is None:
        st.error("Failed to load model. Please refresh the page.")
        return
    
    # Main content tabs
    tab1, tab2, tab3 = st.tabs(["📝 Single Text Analysis", "📋 Batch Analysis", "📈 History"])
    
    with tab1:
        st.subheader("Analyze Single Text")
        
        # Text input
        user_input = st.text_area(
            "Enter text to analyze:",
            height=150,
            placeholder="Type or paste your text here... (e.g., 'I absolutely loved this product! It exceeded my expectations.')"
        )
        
        col1, col2, col3 = st.columns([1, 1, 3])
        with col1:
            analyze_button = st.button("🔍 Analyze Sentiment", type="primary")
        with col2:
            clear_button = st.button("🗑️ Clear")
        
        if clear_button:
            st.rerun()
        
        if analyze_button and user_input:
            with st.spinner("Analyzing..."):
                result = analyze_sentiment(user_input, model)
                
                if result:
                    # Save to history
                    st.session_state.history.append({
                        'text': user_input[:100] + '...' if len(user_input) > 100 else user_input,
                        'label': result['label'],
                        'score': result['score'],
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    })
                    
                    # Display results
                    st.success("Analysis Complete!")
                    
                    col1, col2 = st.columns([1, 1])
                    
                    with col1:
                        st.markdown("### Results")
                        
                        # Sentiment label with color
                        if result['label'] == 'POSITIVE':
                            st.markdown(f"### 😊 **{result['label']}**")
                            st.success(f"Confidence: {result['score']:.2%}")
                        else:
                            st.markdown(f"### 😞 **{result['label']}**")
                            st.error(f"Confidence: {result['score']:.2%}")
                        
                        # Additional metrics
                        st.metric(
                            label="Confidence Level",
                            value=f"{result['score']:.2%}",
                            delta=f"{result['score'] - 0.5:.2%} from neutral"
                        )
                    
                    with col2:
                        # Gauge chart
                        fig = create_sentiment_gauge(result['score'], result['label'])
                        st.plotly_chart(fig, use_container_width=True)
        
        elif analyze_button:
            st.warning("Please enter some text to analyze.")
    
    with tab2:
        st.subheader("Batch Analysis")
        st.markdown("Analyze multiple texts at once. Enter one text per line.")
        
        batch_input = st.text_area(
            "Enter multiple texts (one per line):",
            height=200,
            placeholder="Line 1: First text to analyze\nLine 2: Second text to analyze\nLine 3: Third text to analyze"
        )
        
        if st.button("🔍 Analyze Batch", type="primary"):
            if batch_input:
                texts = [line.strip() for line in batch_input.split('\n') if line.strip()]
                
                if texts:
                    progress_bar = st.progress(0)
                    results = []
                    
                    for i, text in enumerate(texts):
                        result = analyze_sentiment(text, model)
                        if result:
                            results.append({
                                'Text': text[:50] + '...' if len(text) > 50 else text,
                                'Sentiment': result['label'],
                                'Confidence': f"{result['score']:.2%}"
                            })
                        progress_bar.progress((i + 1) / len(texts))
                    
                    progress_bar.empty()
                    
                    # Display results table
                    df = pd.DataFrame(results)
                    st.dataframe(df, use_container_width=True)
                    
                    # Visualization
                    sentiment_counts = df['Sentiment'].value_counts()
                    fig = px.pie(
                        values=sentiment_counts.values,
                        names=sentiment_counts.index,
                        title="Sentiment Distribution",
                        color=sentiment_counts.index,
                        color_discrete_map={'POSITIVE': '#90EE90', 'NEGATIVE': '#FFB6C6'}
                    )
                    st.plotly_chart(fig, use_container_width=True)
                else:
                    st.warning("No valid texts found.")
            else:
                st.warning("Please enter texts to analyze.")
    
    with tab3:
        st.subheader("Analysis History")
        
        if len(st.session_state.history) > 0:
            df_history = pd.DataFrame(st.session_state.history)
            
            # Display history table
            st.dataframe(df_history, use_container_width=True)
            
            # Sentiment over time chart
            fig = px.scatter(
                df_history,
                x='timestamp',
                y='score',
                color='label',
                title="Sentiment Over Time",
                color_discrete_map={'POSITIVE': 'green', 'NEGATIVE': 'red'},
                hover_data=['text']
            )
            st.plotly_chart(fig, use_container_width=True)
            
            # Clear history button
            if st.button("🗑️ Clear History"):
                st.session_state.history = []
                st.rerun()
        else:
            st.info("No analysis history yet. Start analyzing some text!")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center'>
        <p>Built with ❤️ using Streamlit and Hugging Face Transformers</p>
        <p><small>Model: distilbert-base-uncased-finetuned-sst-2-english</small></p>
    </div>
    """, unsafe_allow_html=True)


if __name__ == "__main__":
    main()
