from text_enhancer import TextEnhancer
import json
from pprint import pprint

def main():
    # Sample texts for demonstration
    sample_texts = [
        """Apple Inc. announced its new iPhone 14 today. CEO Tim Cook said it's the best iPhone ever made. 
        The event in Cupertino, California was attended by thousands of people.""",
        
        """The customer service was terrible! I waited for 2 hours and nobody helped me. 
        I'll never shop at this store again. Worst experience ever!!!""",
        
        """The new restaurant on 5th Avenue is amazing! The food was delicious and the staff was very friendly. 
        I highly recommend trying their special pasta dish. Will definitely come back! 😊"""
    ]

    # Initialize TextEnhancer
    enhancer = TextEnhancer()
    
    print("Text Analytics Enhancement Demo")
    print("=" * 50)
    
    # Process each sample text
    for i, text in enumerate(sample_texts, 1):
        print(f"\nAnalyzing Text Sample {i}:")
        print("-" * 30)
        print(f"Original Text: {text}\n")
        
        # Enhance the text
        results = enhancer.enhance_text(text)
        
        # Display results in a formatted way
        print("Normalized Text:")
        print(results['normalized_text'])
        print("\nNamed Entities Found:")
        for entity in results['entities']:
            print(f"- {entity['text']} ({entity['label']})")
        
        print("\nSentiment Analysis:")
        print("TextBlob Results:")
        print(f"- Polarity: {results['sentiment']['textblob_sentiment']['polarity']:.2f}")
        print(f"- Subjectivity: {results['sentiment']['textblob_sentiment']['subjectivity']:.2f}")
        print("Transformer Results:")
        print(f"- Label: {results['sentiment']['transformer_sentiment']['label']}")
        print(f"- Score: {results['sentiment']['transformer_sentiment']['score']:.2f}")
        
        print("\nPOS Tags (first 5):")
        for token, pos in results['pos_tags'][:5]:
            print(f"- {token}: {pos}")
        
        print("=" * 50)

if __name__ == "__main__":
    main() 