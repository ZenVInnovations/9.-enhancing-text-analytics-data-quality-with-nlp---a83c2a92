from text_enhancer import TextEnhancer

def main():
    # Create some example texts
    texts = [
        """Amazon announced record profits in 2023. CEO Andy Jassy said the company's 
        cloud services and AI initiatives were major growth drivers.""",
        
        """I absolutely loved the new restaurant! The food was amazing and the service 
        was exceptional. Will definitely come back again! 😊""",
        
        """The customer support was terrible. I waited for 2 hours and no one responded 
        to my emails. Very disappointed with the service."""
    ]

    print("Initializing Text Enhancer...")
    enhancer = TextEnhancer()

    # Process each text
    for i, text in enumerate(texts, 1):
        print(f"\n{'='*60}")
        print(f"Analyzing Text {i}:")
        print(f"{'='*60}")
        
        print("Original Text:")
        print(text)
        print("\nProcessing...")
        
        # Get enhanced results
        results = enhancer.enhance_text(text)
        
        # Display results
        print("\n1. Normalized Text:")
        print(results['normalized_text'])
        
        print("\n2. Named Entities Found:")
        for entity in results['entities']:
            print(f"- {entity['text']} ({entity['label']})")
        
        print("\n3. Sentiment Analysis:")
        print("TextBlob Results:")
        sentiment = results['sentiment']['textblob_sentiment']
        print(f"- Polarity: {sentiment['polarity']:.2f} (-1 to 1, negative to positive)")
        print(f"- Subjectivity: {sentiment['subjectivity']:.2f} (0 to 1, objective to subjective)")
        
        print("\nTransformer Results:")
        transformer_sentiment = results['sentiment']['transformer_sentiment']
        print(f"- Label: {transformer_sentiment['label']}")
        print(f"- Confidence: {transformer_sentiment['score']:.2%}")
        
        print("\n4. First 5 Words with POS Tags:")
        for token, pos in results['pos_tags'][:5]:
            print(f"- {token}: {pos}")

if __name__ == "__main__":
    main() 