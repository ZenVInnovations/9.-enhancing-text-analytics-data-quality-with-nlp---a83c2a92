# Text Analytics Enhancement with NLP

This project demonstrates advanced NLP techniques for enhancing text data quality. It includes functionality for text normalization, named entity recognition, and sentiment analysis.

## Features

- Text normalization and cleaning
- Named Entity Recognition (NER)
- Dual sentiment analysis (TextBlob and Transformers)
- Part-of-speech tagging
- Comprehensive error handling and logging

## Installation

1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```
3. Download the spaCy English model:
```bash
python -m spacy download en_core_web_sm
```

## Usage

The project includes two main files:

1. `text_enhancer.py`: The main module containing the TextEnhancer class
2. `demo.py`: A demonstration script showing how to use the TextEnhancer

To run the demo:
```bash
python demo.py
```

### Example Usage in Your Code

```python
from text_enhancer import TextEnhancer

# Initialize the enhancer
enhancer = TextEnhancer()

# Process some text
text = "Apple Inc. announced its new iPhone today in California!"
results = enhancer.enhance_text(text)

# Access the results
print(results['normalized_text'])  # Normalized text
print(results['entities'])         # Named entities
print(results['sentiment'])        # Sentiment analysis results
print(results['pos_tags'])        # Part-of-speech tags
```

## Output Format

The `enhance_text()` method returns a dictionary containing:

- `original_text`: The input text
- `normalized_text`: Cleaned and normalized text
- `entities`: List of named entities with their labels
- `sentiment`: Sentiment analysis results from both TextBlob and Transformers
- `tokens`: List of tokenized words
- `pos_tags`: List of (token, POS tag) pairs

## Error Handling

The module includes comprehensive error handling and logging. All errors are logged and can be found in the application logs.

## Requirements

See `requirements.txt` for a complete list of dependencies. Main requirements include:

- spacy>=3.7.2
- nltk>=3.8.1
- textblob>=0.17.1
- transformers>=4.36.0
- cleantext>=1.1.4

## License

This project is licensed under the MIT License. 