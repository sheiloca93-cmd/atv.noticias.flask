
from flask import Flask, jsonify, request

app = Flask(__name__)

noticias = []

@app.route('/')
def home():
    return jsonify({"mensagem": "API de Notícias funcionando!"})

if __name__ == '__main__':
    app.run(debug=True)




