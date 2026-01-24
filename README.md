# 🎭 Sentiment Analysis Dashboard

A production-ready web application for real-time sentiment analysis using state-of-the-art transformer models. Built with Streamlit and Hugging Face Transformers.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)
![Transformers](https://img.shields.io/badge/Transformers-4.36.2-yellow.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 🌟 Features

- **Real-time Sentiment Analysis**: Instantly analyze the sentiment of any text input
- **Batch Processing**: Analyze multiple texts simultaneously
- **Interactive Visualizations**: Beautiful charts and gauges showing sentiment scores
- **Analysis History**: Track all your previous analyses with timestamps
- **Confidence Scoring**: See how confident the AI is about each prediction
- **Responsive UI**: Clean, modern interface that works on all devices

## 🚀 Live Demo

[Add your deployed app link here after deployment]

## 🧠 How It Works

This application uses a pre-trained **DistilBERT** model fine-tuned on the SST-2 (Stanford Sentiment Treebank) dataset. The model achieves state-of-the-art performance with:

- **Model**: `distilbert-base-uncased-finetuned-sst-2-english`
- **Architecture**: Transformer-based (DistilBERT)
- **Task**: Binary sentiment classification (Positive/Negative)
- **Accuracy**: ~91% on SST-2 test set

### Technical Pipeline

1. **Input Processing**: Text is tokenized using DistilBERT tokenizer
2. **Model Inference**: Processed through 6-layer transformer network
3. **Classification**: Outputs probability distribution over sentiment classes
4. **Visualization**: Results displayed with confidence scores and interactive charts

## 📋 Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- 2GB RAM minimum (4GB recommended)
- Internet connection (for first-time model download)

## 🛠️ Installation

### Option 1: Quick Start (Recommended for Beginners)

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/sentiment-analysis-app.git
cd sentiment-analysis-app
```

2. **Create a virtual environment** (recommended)
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, manually navigate to that URL

### Option 2: Using Docker (Advanced)

```bash
docker build -t sentiment-app .
docker run -p 8501:8501 sentiment-app
```

## 💻 Usage

### Single Text Analysis

1. Navigate to the "Single Text Analysis" tab
2. Enter your text in the input box
3. Click "Analyze Sentiment"
4. View the results, confidence score, and visualization

### Batch Analysis

1. Go to the "Batch Analysis" tab
2. Enter multiple texts (one per line)
3. Click "Analyze Batch"
4. See results table and sentiment distribution chart

### View History

1. Click the "History" tab
2. See all your previous analyses
3. Explore sentiment trends over time
4. Clear history if needed

## 📁 Project Structure

```
sentiment-analysis-app/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── .gitignore             # Git ignore file
├── Dockerfile             # Docker configuration (optional)
└── screenshots/           # App screenshots (for README)
    ├── main.png
    ├── batch.png
    └── history.png
```

## 🎯 Key Technical Highlights

### 1. **Model Optimization**
- Uses `@st.cache_resource` for efficient model loading
- Single model instance shared across all requests
- GPU acceleration support (automatic CUDA detection)

### 2. **Error Handling**
- Graceful degradation when model fails to load
- Input validation and text truncation
- User-friendly error messages

### 3. **Performance**
- Lazy loading of transformer model
- Efficient batch processing
- Minimal memory footprint

### 4. **Code Quality**
- Clean, well-documented code
- Modular function design
- PEP 8 style compliance
- Type hints and docstrings

## 🧪 Testing

```bash
# Run basic functionality test
python -c "from transformers import pipeline; print('Setup successful!')"
```

## 📊 Model Performance

| Metric | Score |
|--------|-------|
| Accuracy | 91.3% |
| F1 Score | 91.1% |
| Inference Speed | ~50ms per text |
| Model Size | 255MB |


## 🎓 Learning Resources

This project demonstrates several important concepts:

- **Natural Language Processing (NLP)**
- **Transformer Models**
- **Transfer Learning**
- **Web Application Development**
- **Data Visualization**
- **Software Engineering Best Practices**

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🐛 Troubleshooting

**Problem**: Model takes too long to load
- **Solution**: First download is ~255MB. Subsequent loads use cached model.

**Problem**: Out of memory error
- **Solution**: Close other applications or use a machine with more RAM.

**Problem**: App won't start
- **Solution**: Ensure all dependencies are installed: `pip install -r requirements.txt`

## 📝 Future Enhancements

- [ ] Multi-language support
- [ ] Emotion detection (beyond positive/negative)
- [ ] Integration with social media APIs
- [ ] Export results to CSV/PDF
- [ ] Custom model training interface
- [ ] A/B testing different models
- [ ] Real-time streaming data analysis

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: @4ktLuffy
- LinkedIn: https://www.linkedin.com/in/henos-dereje-221aa2215/
- Email: henosd19@gmail.com

## 🙏 Acknowledgments

- [Hugging Face](https://huggingface.co/) for the amazing Transformers library
- [Streamlit](https://streamlit.io/) for the easy-to-use web framework
- [Stanford NLP](https://nlp.stanford.edu/) for the SST-2 dataset
- The open-source community

## 📸 Screenshots

### Main Interface
![Main Interface](screenshots/main.png)

### Batch Analysis
![Batch Analysis](screenshots/batch.png)

### History View
![History](screenshots/history.png)

---

⭐ If you found this project helpful, please give it a star!
