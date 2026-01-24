# 📝 Quick Reference Guide

## Common Commands

### Setting Up
```bash
# Clone repository
git clone https://github.com/YOUR-USERNAME/sentiment-analysis-app.git
cd sentiment-analysis-app

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt

# Test installation
python test_setup.py
```

### Running the App
```bash
# Start the app
streamlit run app.py

# Access at: http://localhost:8501
```

### Git Commands
```bash
# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Your message here"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main
```

### Python Environment
```bash
# Activate virtual environment
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate      # Windows

# Deactivate virtual environment
deactivate

# Update packages
pip install --upgrade -r requirements.txt

# Check installed packages
pip list

# Save current packages
pip freeze > requirements.txt
```

### Streamlit Specific
```bash
# Run with specific port
streamlit run app.py --server.port 8502

# Run without opening browser
streamlit run app.py --server.headless true

# Clear cache
streamlit cache clear

# Show config
streamlit config show
```

### Docker Commands (if using Docker)
```bash
# Build image
docker build -t sentiment-app .

# Run container
docker run -p 8501:8501 sentiment-app

# Stop container
docker stop <container-id>

# List running containers
docker ps
```

## Project Structure
```
sentiment-analysis-app/
│
├── app.py              # Main application
├── test_setup.py       # Installation test
├── requirements.txt    # Dependencies
├── README.md          # Documentation
├── SETUP_GUIDE.md     # Beginner guide
├── LICENSE            # MIT License
├── .gitignore         # Git ignore
├── Dockerfile         # Docker config
│
└── venv/              # Virtual environment (not in git)
```

## Useful Resources

### Documentation
- [Streamlit Docs](https://docs.streamlit.io)
- [Transformers Docs](https://huggingface.co/docs/transformers)
- [PyTorch Docs](https://pytorch.org/docs)

### Deployment
- [Streamlit Cloud](https://share.streamlit.io)
- [Hugging Face Spaces](https://huggingface.co/spaces)
- [Heroku](https://www.heroku.com)

### Learning
- [Hugging Face Course](https://huggingface.co/course)
- [Streamlit Gallery](https://streamlit.io/gallery)
- [ML Tutorials](https://www.tensorflow.org/tutorials)

## Troubleshooting

### "Module not found" error
```bash
pip install -r requirements.txt --upgrade
```

### "Port already in use"
```bash
# Use different port
streamlit run app.py --server.port 8502
```

### "Out of memory"
- Close other applications
- Restart your computer
- Use a machine with more RAM

### Model loading issues
- Check internet connection
- Clear cache: `rm -rf ~/.cache/huggingface`
- Redownload model by running test_setup.py

## Performance Tips

1. **First run is slow** - Model downloads ~255MB
2. **Subsequent runs are fast** - Model is cached
3. **Use GPU if available** - Automatically detected
4. **Close unused tabs** - Saves memory
5. **Restart if sluggish** - Clears memory

## Security Notes

- Never commit `.env` files
- Don't share API keys in code
- Keep dependencies updated
- Use virtual environments
- Review code before deployment

## Making Changes

### Add new feature
1. Create new branch: `git checkout -b new-feature`
2. Make changes
3. Test thoroughly
4. Commit: `git commit -m "Add new feature"`
5. Push: `git push origin new-feature`
6. Create Pull Request on GitHub

### Update README
- Keep documentation current
- Add screenshots
- Update feature list
- Include deployment URL

## Interview Talking Points

### Technical Skills Demonstrated
- Natural Language Processing (NLP)
- Transformer models (BERT/DistilBERT)
- Transfer learning
- Web development (Streamlit)
- Data visualization (Plotly)
- Version control (Git)
- Deployment (Cloud platforms)
- Python best practices

### Project Complexity
- Production-ready code
- Error handling
- Performance optimization
- Modular design
- Comprehensive documentation
- Testing procedures
- Deployment pipeline

### Business Value
- Real-world application
- User-friendly interface
- Scalable architecture
- Low latency (<100ms)
- Cost-effective (free deployment)
- Maintainable codebase
