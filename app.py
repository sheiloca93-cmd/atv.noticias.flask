
from flask import Flask, jsonify, request

app = Flask(__name__)

noticias = [
    {
      "titulo": "Notícia 1",
        "conteudo": "Conteúdo da notícia 1"
    },
    {
      "titulo": "Notícia 2",
        "conteudo": "Conteúdo da notícia 2"
    },
    {
      "titulo": "Notícia 3",
        "conteudo": "Conteúdo da notícia 3"
    }
]

@app.get('/noticias')
def get_noticias():
    return {"noticias": noticias}



