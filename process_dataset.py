import pandas as pd
import json
from text_enhancer import TextEnhancer
from datetime import datetime
import os

def process_dataset(input_file, output_dir):
    """
    Process the dataset and save results to both JSON and CSV formats.
    
    Args:
        input_file (str): Path to input CSV file
        output_dir (str): Directory to save output files
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read the input dataset
    print("Reading dataset...")
    df = pd.read_csv(input_file)
    
    # Initialize the text enhancer
    print("Initializing TextEnhancer...")
    enhancer = TextEnhancer()
    
    # Process each text and store results
    results = []
    total = len(df)
    
    print(f"Processing {total} texts...")
    for idx, row in df.iterrows():
        print(f"Processing text {idx + 1}/{total}...")
        
        # Get enhanced text analysis
        analysis = enhancer.enhance_text(row['content'])
        
        # Create result dictionary
        result = {
            'text_id': row['text_id'],
            'category': row['category'],
            'original_text': row['content'],
            'normalized_text': analysis['normalized_text'],
            'entities': analysis['entities'],
            'sentiment_polarity': analysis['sentiment']['textblob_sentiment']['polarity'],
            'sentiment_subjectivity': analysis['sentiment']['textblob_sentiment']['subjectivity'],
            'transformer_sentiment': analysis['sentiment']['transformer_sentiment']['label'],
            'transformer_confidence': analysis['sentiment']['transformer_sentiment']['score'],
            'tokens': analysis['tokens'],
            'pos_tags': analysis['pos_tags']
        }
        results.append(result)
    
    # Generate timestamp for file names
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Save detailed results to JSON
    json_file = os.path.join(output_dir, f'text_analysis_detailed_{timestamp}.json')
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # Create simplified DataFrame for CSV
    csv_results = []
    for r in results:
        csv_result = {
            'text_id': r['text_id'],
            'category': r['category'],
            'normalized_text': r['normalized_text'],
            'sentiment_polarity': r['sentiment_polarity'],
            'sentiment_subjectivity': r['sentiment_subjectivity'],
            'transformer_sentiment': r['transformer_sentiment'],
            'transformer_confidence': r['transformer_confidence'],
            'entity_count': len(r['entities']),
            'token_count': len(r['tokens'])
        }
        csv_results.append(csv_result)
    
    # Save simplified results to CSV
    csv_file = os.path.join(output_dir, f'text_analysis_summary_{timestamp}.csv')
    pd.DataFrame(csv_results).to_csv(csv_file, index=False)
    
    print("\nProcessing complete!")
    print(f"Detailed results saved to: {json_file}")
    print(f"Summary results saved to: {csv_file}")
    
    return json_file, csv_file

if __name__ == "__main__":
    # Process the dataset
    input_file = "sample_data.csv"
    output_dir = "results"
    
    try:
        json_file, csv_file = process_dataset(input_file, output_dir)
        
        # Print some statistics from the CSV file
        print("\nAnalysis Summary:")
        df = pd.read_csv(csv_file)
        print("\nSentiment Distribution:")
        print(df['transformer_sentiment'].value_counts())
        print("\nAverage Sentiment Polarity by Category:")
        print(df.groupby('category')['sentiment_polarity'].mean().round(2))
        
    except Exception as e:
        print(f"Error processing dataset: {str(e)}") 