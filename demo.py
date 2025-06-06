from text_analyzer import TextAnalyzer
import json

def print_analysis_results(results):
    """
    Pretty print the analysis results
    """
    print("\n=== Text Analysis Results ===")
    print("\nOriginal Text:")
    print(results['original_text'])
    
    print("\nCleaned Text:")
    print(results['cleaned_text'])
    
    print("\nNamed Entities:")
    for entity_type, entities in results['entities'].items():
        print(f"{entity_type}: {', '.join(entities)}")
    
    print("\nSentiment Analysis:")
    print("TextBlob Scores:")
    print(f"Polarity: {results['sentiment']['textblob_sentiment']['polarity']:.2f}")
    print(f"Subjectivity: {results['sentiment']['textblob_sentiment']['subjectivity']:.2f}")
    
    print("\nOverall Sentiment:")
    print(f"Label: {results['sentiment']['overall_sentiment']['label']}")
    print(f"Confidence Score: {results['sentiment']['overall_sentiment']['score']:.2f}")

def main():
    # Initialize the text analyzer
    analyzer = TextAnalyzer()
    
    # Example texts
    sample_texts = [
        """Apple Inc. CEO Tim Cook announced their latest iPhone 14 Pro Max 
        at their headquarters in Cupertino. The new device received excellent 
        reviews from tech enthusiasts and customers alike.""",
        
        """The restaurant's service was terrible! We waited for over an hour 
        for our food, and when it finally arrived, it was cold. I would not 
        recommend this place to anyone.""",
        
        """The new climate change policy implemented by the European Union 
        aims to reduce carbon emissions by 55% before 2030. Environmental 
        activists are optimistic about this development."""
    ]
    
    # Analyze each text
    for i, text in enumerate(sample_texts, 1):
        print(f"\n{'='*50}")
        print(f"Example {i}:")
        results = analyzer.analyze_text(text)
        print_analysis_results(results)

if __name__ == "__main__":
    main() 