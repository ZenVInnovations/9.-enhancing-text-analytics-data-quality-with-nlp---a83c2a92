import nltk
from textblob import TextBlob
from typing import Dict, List, Any
import logging
from transformers import pipeline
import re

# Download required NLTK data
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Initialize logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TextEnhancer:
    def __init__(self):
        """Initialize the TextEnhancer with required models and tools."""
        try:
            # Initialize sentiment analyzer from transformers
            self.sentiment_analyzer = pipeline("sentiment-analysis")
            # Initialize NER pipeline from transformers
            self.ner_pipeline = pipeline("ner")
            logger.info("Successfully initialized TextEnhancer")
        except Exception as e:
            logger.error(f"Error initializing TextEnhancer: {str(e)}")
            raise

    def normalize_text(self, text: str) -> str:
        """
        Normalize text by cleaning and standardizing it.
        
        Args:
            text (str): Input text to normalize
            
        Returns:
            str: Normalized text
        """
        try:
            # Basic text normalization
            text = text.lower()
            # Remove URLs
            text = re.sub(r'http\S+|www.\S+', '', text)
            # Remove email addresses
            text = re.sub(r'\S+@\S+', '', text)
            # Remove extra whitespace
            text = ' '.join(text.split())
            return text
        except Exception as e:
            logger.error(f"Error in text normalization: {str(e)}")
            return text

    def extract_entities(self, text: str) -> List[Dict[str, Any]]:
        """
        Extract named entities from text using transformers NER pipeline.
        
        Args:
            text (str): Input text for entity extraction
            
        Returns:
            List[Dict]: List of extracted entities with their labels
        """
        try:
            # Use transformers NER pipeline
            entities = self.ner_pipeline(text)
            
            # Format entities to match the previous output structure
            formatted_entities = [
                {
                    'text': entity['word'],
                    'label': entity['entity'],
                    'start': entity['start'],
                    'end': entity['end']
                }
                for entity in entities
            ]
            return formatted_entities
        except Exception as e:
            logger.error(f"Error in entity extraction: {str(e)}")
            return []

    def analyze_sentiment(self, text: str) -> Dict[str, Any]:
        """
        Perform sentiment analysis using both TextBlob and Transformers.
        
        Args:
            text (str): Input text for sentiment analysis
            
        Returns:
            Dict: Sentiment analysis results
        """
        try:
            # TextBlob sentiment
            blob = TextBlob(text)
            textblob_sentiment = {
                'polarity': blob.sentiment.polarity,
                'subjectivity': blob.sentiment.subjectivity
            }

            # Transformers sentiment
            transformer_sentiment = self.sentiment_analyzer(text)[0]

            return {
                'textblob_sentiment': textblob_sentiment,
                'transformer_sentiment': transformer_sentiment
            }
        except Exception as e:
            logger.error(f"Error in sentiment analysis: {str(e)}")
            return {}

    def get_pos_tags(self, text: str) -> List[tuple]:
        """
        Get part-of-speech tags using TextBlob.
        
        Args:
            text (str): Input text
            
        Returns:
            List[tuple]: List of (token, POS tag) pairs
        """
        try:
            # Use TextBlob for POS tagging
            blob = TextBlob(text)
            return [(str(word), tag) for word, tag in blob.tags]
        except Exception as e:
            logger.error(f"Error in POS tagging: {str(e)}")
            return []

    def enhance_text(self, text: str) -> Dict[str, Any]:
        """
        Enhance text by applying all available NLP techniques.
        
        Args:
            text (str): Input text to enhance
            
        Returns:
            Dict: Enhanced text data with all analyses
        """
        try:
            # Initialize empty result dictionary
            result = {
                'original_text': text,
                'normalized_text': text,
                'entities': [],
                'sentiment': {'textblob_sentiment': {'polarity': 0.0, 'subjectivity': 0.0},
                            'transformer_sentiment': {'label': 'NEUTRAL', 'score': 0.0}},
                'tokens': [],
                'pos_tags': []
            }
            
            # Normalize text
            result['normalized_text'] = self.normalize_text(text)
            
            # Extract entities
            result['entities'] = self.extract_entities(text)
            
            # Analyze sentiment
            result['sentiment'] = self.analyze_sentiment(text)
            
            # Get POS tags and tokens
            result['pos_tags'] = self.get_pos_tags(text)
            result['tokens'] = [token for token, _ in result['pos_tags']]
            
            return result
        except Exception as e:
            logger.error(f"Error in text enhancement: {str(e)}")
            return result 