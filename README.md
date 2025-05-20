# Text Analysis Web Application

A powerful web-based text analysis tool that provides sentiment analysis, named entity recognition, and text preprocessing capabilities. Built with Python, Flask, and modern NLP libraries.

## Features

- **Text Preprocessing**
  - Text normalization
  - Stopword removal
  - Lemmatization
  - Spelling correction

- **Sentiment Analysis**
  - Polarity detection (positive/negative/neutral)
  - Subjectivity analysis
  - Confidence scoring

- **Named Entity Recognition**
  - Person names
  - Organizations
  - Locations
  - Dates
  - And more...

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd text-analysis-webapp
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Download required NLTK data:
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet'); nltk.download('averaged_perceptron_tagger')"
```

5. Download spaCy model:
```bash
python -m spacy download en_core_web_sm
```

## Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

## Usage

1. Enter or paste your text in the input area
2. Click the "Analyze Text" button
3. View the analysis results:
   - Cleaned text
   - Named entities
   - Sentiment analysis scores

## Project Structure

```
text-analysis-webapp/
├── app.py                 # Flask application
├── text_analyzer.py       # Text analysis logic
├── text_preprocessor.py   # Text preprocessing utilities
├── templates/
│   └── index.html        # Web interface
└── requirements.txt      # Project dependencies
```

## Dependencies

- Flask: Web framework
- spaCy: NLP library for entity recognition
- NLTK: Natural Language Toolkit
- TextBlob: Sentiment analysis
- Other dependencies listed in requirements.txt

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- spaCy for NLP capabilities
- NLTK for text processing
- TextBlob for sentiment analysis
- Flask for the web framework 