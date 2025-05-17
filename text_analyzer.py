import spacy
from textblob import TextBlob
from text_preprocessor import TextPreprocessor

class TextAnalyzer:
    def __init__(self):
        # Initialize spaCy model
        self.nlp = spacy.load("en_core_web_sm")
        # Initialize text preprocessor
        self.preprocessor = TextPreprocessor()

    def extract_entities(self, text):
        """
        Extract named entities from text using spaCy
        """
        # Preprocess text
        cleaned_text = self.preprocessor.process_text(text, 
                                                    remove_stops=False, 
                                                    lemmatize=False)
        # Process text with spaCy
        doc = self.nlp(cleaned_text)
        
        # Extract entities
        entities = {}
        for ent in doc.ents:
            if ent.label_ not in entities:
                entities[ent.label_] = []
            entities[ent.label_].append(ent.text)
        
        return entities

    def analyze_sentiment(self, text):
        """
        Perform sentiment analysis using TextBlob
        """
        # Preprocess text
        cleaned_text = self.preprocessor.process_text(text, 
                                                    remove_stops=False, 
                                                    lemmatize=False)
        
        # TextBlob sentiment analysis
        blob = TextBlob(cleaned_text)
        sentiment_score = blob.sentiment.polarity
        
        # Determine sentiment label based on polarity
        if sentiment_score > 0:
            sentiment_label = "POSITIVE"
        elif sentiment_score < 0:
            sentiment_label = "NEGATIVE"
        else:
            sentiment_label = "NEUTRAL"
        
        return {
            'textblob_sentiment': {
                'polarity': sentiment_score,
                'subjectivity': blob.sentiment.subjectivity
            },
            'overall_sentiment': {
                'label': sentiment_label,
                'score': abs(sentiment_score)
            }
        }

    def analyze_text(self, text):
        """
        Perform comprehensive text analysis
        """
        # Clean and preprocess text
        cleaned_text = self.preprocessor.process_text(text)
        
        # Perform various analyses
        analysis_results = {
            'original_text': text,
            'cleaned_text': cleaned_text,
            'entities': self.extract_entities(text),
            'sentiment': self.analyze_sentiment(text)
        }
        
        return analysis_results 