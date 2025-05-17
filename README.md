# Text Analytics with NLP

This project provides a comprehensive solution for enhancing text analytics data quality using advanced NLP techniques. It includes functionality for text normalization, entity recognition, and sentiment analysis.

## Features

- Text preprocessing and normalization
- Spelling correction
- Stopword removal
- Lemmatization
- Named Entity Recognition (NER)
- Sentiment Analysis (using both TextBlob and Transformers)

## Setup

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Download the spaCy English model:
```bash
python -m spacy download en_core_web_sm
```

## Usage

The project consists of three main components:

1. `text_preprocessor.py`: Handles text cleaning and normalization
2. `text_analyzer.py`: Provides entity recognition and sentiment analysis
3. `demo.py`: Demonstrates the usage of the text analytics functionality

To run the demo:
```bash
python demo.py
```

## Example Usage

```python
from text_analyzer import TextAnalyzer

# Create an analyzer instance
analyzer = TextAnalyzer()

# Analyze your text
your_text = "Your text goes here"
results = analyzer.analyze_text(your_text)

# The results will contain:
print(results['original_text'])  # Your original text
print(results['cleaned_text'])   # Preprocessed text
print(results['entities'])       # Named entities found
print(results['sentiment'])      # Sentiment analysis results
```

## Output Format

The analysis results include:
- Original text
- Cleaned text
- Named entities (categorized by type)
- Sentiment analysis results from both TextBlob and Transformers
  - TextBlob: Polarity and subjectivity scores
  - Transformers: Sentiment label and confidence score 
