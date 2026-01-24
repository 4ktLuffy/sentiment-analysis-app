"""
Simple test script to verify the sentiment analysis setup
Run this to make sure everything is installed correctly
"""

import sys

def test_imports():
    """Test if all required packages can be imported"""
    print("Testing imports...")
    
    try:
        import streamlit
        print("✓ Streamlit imported successfully")
    except ImportError:
        print("✗ Failed to import Streamlit")
        return False
    
    try:
        import transformers
        print("✓ Transformers imported successfully")
    except ImportError:
        print("✗ Failed to import Transformers")
        return False
    
    try:
        import torch
        print("✓ PyTorch imported successfully")
    except ImportError:
        print("✗ Failed to import PyTorch")
        return False
    
    try:
        import pandas
        print("✓ Pandas imported successfully")
    except ImportError:
        print("✗ Failed to import Pandas")
        return False
    
    try:
        import plotly
        print("✓ Plotly imported successfully")
    except ImportError:
        print("✗ Failed to import Plotly")
        return False
    
    return True


def test_model_loading():
    """Test if the sentiment analysis model can be loaded"""
    print("\nTesting model loading...")
    
    try:
        from transformers import pipeline
        
        print("Loading sentiment analysis model...")
        print("(This may take a few minutes on first run)")
        
        sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )
        
        print("✓ Model loaded successfully")
        
        # Test prediction
        print("\nTesting prediction...")
        test_text = "I love this amazing product!"
        result = sentiment_pipeline(test_text)[0]
        
        print(f"Test text: '{test_text}'")
        print(f"Prediction: {result['label']} (confidence: {result['score']:.2%})")
        print("✓ Prediction successful")
        
        return True
        
    except Exception as e:
        print(f"✗ Error: {str(e)}")
        return False


def main():
    print("=" * 60)
    print("Sentiment Analysis App - Installation Test")
    print("=" * 60)
    print()
    
    # Test imports
    if not test_imports():
        print("\n❌ Import test failed!")
        print("Run: pip install -r requirements.txt")
        sys.exit(1)
    
    # Test model
    if not test_model_loading():
        print("\n❌ Model loading test failed!")
        print("Check your internet connection and try again")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("🎉 All tests passed! Your setup is complete!")
    print("=" * 60)
    print("\nYou can now run the app with:")
    print("  streamlit run app.py")
    print()


if __name__ == "__main__":
    main()
