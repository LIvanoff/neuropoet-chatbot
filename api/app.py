# app.py
from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)

# Инициализация модели
llm = pipeline("text-generation", model="gpt2")  # Можно заменить на более подходящую модель

@app.route('/generate', methods=['POST'])
def generate_text():
    data = request.json
    prompt = data.get('prompt', '')
    response = llm(prompt, max_length=100, num_return_sequences=1)
    return jsonify(response[0]["generated_text"])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
