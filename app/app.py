from flask import Flask, jsonify, render_template
import random

app = Flask(__name__)

quotes = [
    "The best way to predict the future is to invent it.",
    "Life is what happens when you're busy making other plans.",
    "Do or do not. There is no try.",
    "Stay hungry, stay foolish.",
    "In the middle of every difficulty lies opportunity."
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/quote')
def random_quote():
    return jsonify({'quote': random.choice(quotes)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
