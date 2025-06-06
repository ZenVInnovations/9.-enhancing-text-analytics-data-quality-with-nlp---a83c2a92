from flask import Flask, render_template, request, jsonify
from text_analyzer import TextAnalyzer
import json

app = Flask(__name__)
analyzer = TextAnalyzer()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    try:
        results = analyzer.analyze_text(text)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 