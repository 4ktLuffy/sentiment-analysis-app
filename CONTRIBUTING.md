# Contributing to Sentiment Analysis Dashboard

Thank you for your interest in contributing! This document provides guidelines for contributing to this project.

## How to Contribute

### Reporting Bugs

If you find a bug, please create an issue with:
- Clear description of the problem
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable
- Your environment (OS, Python version)

### Suggesting Enhancements

Enhancement suggestions are welcome! Please include:
- Clear description of the feature
- Use cases and benefits
- Possible implementation approach
- Any relevant examples

### Pull Requests

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Make your changes**
   - Write clean, documented code
   - Follow existing code style
   - Add comments where needed
   
4. **Test your changes**
   ```bash
   python test_setup.py
   streamlit run app.py
   ```

5. **Commit your changes**
   ```bash
   git commit -m "Add some AmazingFeature"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/AmazingFeature
   ```

7. **Open a Pull Request**
   - Describe your changes clearly
   - Reference any related issues
   - Include screenshots for UI changes

## Code Style Guidelines

### Python
- Follow PEP 8 style guide
- Use meaningful variable names
- Add docstrings to functions
- Keep functions focused and small
- Use type hints where appropriate

Example:
```python
def analyze_sentiment(text: str, model) -> dict:
    """
    Analyze sentiment of given text.
    
    Args:
        text: Input text to analyze
        model: Loaded sentiment pipeline
    
    Returns:
        dict: Sentiment result with label and score
    """
    # Function implementation
```

### Documentation
- Update README.md for new features
- Add comments for complex logic
- Include usage examples
- Keep documentation current

### Git Commits
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, Remove)
- Keep commits focused on single changes

Examples:
```
✓ Add batch analysis feature
✓ Fix memory leak in model caching
✓ Update deployment documentation
✗ Fixed stuff
✗ Changes
```

## Development Setup

1. Clone your fork
2. Set up virtual environment
3. Install dependencies with dev tools:
   ```bash
   pip install -r requirements.txt
   pip install black flake8 pytest  # Dev tools
   ```

## Testing

- Test all changes locally before pushing
- Ensure app runs without errors
- Test on different browsers if UI changes
- Verify deployment configuration

## Feature Ideas

Looking for contribution ideas? Here are some features we'd love to see:

- [ ] Multi-language sentiment analysis
- [ ] Emotion detection (joy, anger, sadness, etc.)
- [ ] Export results to CSV/PDF
- [ ] API endpoint for programmatic access
- [ ] Social media integration (Twitter, Reddit)
- [ ] Sentiment trend analysis over time
- [ ] Custom model training interface
- [ ] Dark mode theme
- [ ] Mobile responsiveness improvements
- [ ] Performance optimizations

## Questions?

Feel free to:
- Open an issue for questions
- Reach out via email (see README)
- Join discussions in issues/PRs

## Code of Conduct

### Our Pledge

We are committed to providing a welcoming and inspiring community for all.

### Our Standards

**Positive behavior includes:**
- Being respectful and inclusive
- Gracefully accepting constructive criticism
- Focusing on what's best for the community
- Showing empathy towards others

**Unacceptable behavior includes:**
- Harassment or discriminatory language
- Trolling or insulting comments
- Publishing others' private information
- Other conduct inappropriate in a professional setting

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be acknowledged in:
- README.md contributors section
- Release notes for their contributions
- Special thanks in documentation

Thank you for contributing! 🎉
