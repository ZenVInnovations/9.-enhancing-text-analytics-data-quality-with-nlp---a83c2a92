import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from textblob import TextBlob

# Download required NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

class TextPreprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))

    def normalize_text(self, text):
        """
        Normalize text by converting to lowercase and removing special characters
        """
        # Convert to lowercase
        text = text.lower()
        # Remove special characters and numbers
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        # Remove extra whitespace
        text = ' '.join(text.split())
        return text

    def remove_stopwords(self, text):
        """
        Remove common stopwords from text
        """
        words = word_tokenize(text)
        filtered_words = [word for word in words if word not in self.stop_words]
        return ' '.join(filtered_words)

    def lemmatize_text(self, text):
        """
        Lemmatize text to convert words to their base form
        """
        words = word_tokenize(text)
        lemmatized_words = [self.lemmatizer.lemmatize(word) for word in words]
        return ' '.join(lemmatized_words)

    def correct_spelling(self, text):
        """
        Correct spelling errors using TextBlob
        """
        return str(TextBlob(text).correct())

    def process_text(self, text, normalize=True, remove_stops=True, 
                    lemmatize=True, spell_check=True):
        """
        Apply all text preprocessing steps
        """
        if normalize:
            text = self.normalize_text(text)
        if spell_check:
            text = self.correct_spelling(text)
        if remove_stops:
            text = self.remove_stopwords(text)
        if lemmatize:
            text = self.lemmatize_text(text)
        return text 