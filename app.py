from flask import Flask, jsonify, request
from flask_smorest import abort
import os
import uuid

from db import noticias, conteudos

app = Flask(__name__)

### Endpoints de Noticias

# Get /noticias
@app.get('/noticias')
def get_noticias():
    return jsonify({"Noticias":  list( noticias.values())}), 200


# Get /noticia/1
@app.get('/noticia/<string:id_noticia>')
def get_noticia_by_id(id_noticia):
    try:
        return jsonify(noticias[id_noticia]), 200
    except KeyError:
        abort(404, message="Notícia não encontrada")


# Get /noticia?nome=XPTO
@app.get('/noticia')
def get_noticia_by_name():
    nome = request.args('nome')

    for noticia in noticias.values():
        if noticia["nome"] == name:
            return jsonify(noticia), 200
        
    abort(404, message="Notícia não encontrada")


# Post /noticia
## Body > raw > Json
@app.post('/noticia')
def criar_noticia():
    noticia_dado = request.get_json()
    noticia_id = uuid.uuid4().hex

    noticia_nova = {**noticia_dado, "id": noticia_id}

    noticias[noticia_id] = noticia_nova

    return jsonify(noticia_nova), 201
    


# Put /noticia
@app.put('/noticia/<string:id_noticia>')
def atualizar_noticia(id_noticia):

    dado_novo = request.get_json()

    for noticia in noticias.values():
        if noticia["id"] == id_noticia:

            noticia.update(dado_novo)

            return jsonify({"noticia atualizada": noticia}), 200
        
    return jsonify({"erro": "Notícia não encontrada"}), 404


# Delete /noticia/<id_noticia>
@app.delete('/noticia/<string:id_noticia>')
def deletar_noticia(id_noticia):
    try:
        noticias.pop(id_noticia)
        return jsonify({"mensagem": "Notícia removida com sucesso"}), 200
    except KeyError:
        abort(404, message="Notícia não encontrada")        



### Endpoints de conteudos

# Get /conteudos
@app.get('/conteudos')
def buscar_todos_conteudos():
    return jsonify({"Conteúdos": list(conteudos.values())}), 200

#POST /conteudos
@app.post('/conteudos')
def cadastrar_novo_conteudo():        
    conteudos_dado = request.get_json()
    conteudo_id = uuid.uuid4().hex

    conteudo_novo = {**conteudos_dado, "id": conteudo_id}

    conteudos[conteudo_id] = conteudo_novo

    return jsonify(conteudo_novo), 201


#Get /conteudo/<stringid_conteudo>
@app.get('/conteudo/<string:id_conteudo>')
def buscar_conteudo_por_id(id_conteudo):
    try:
        return jsonify(conteudos[id_conteudo])
    except KeyError:
        abort(404, message="Conteúdo não encontrado")   


#DELITE /conteudo/<stringid_conteudo>
@app.delete('/conteudo/<string:id_conteudo>')
def deletar_conteudo_por_id(id_conteudo):
    try:
        conteudos.pop(id_conteudo)
        return jsonify({"mensagem": "Conteúdo removido com sucesso"}), 200
    except KeyError:
        abort(404, message="Notícia não encontrada")



#PUT / conteudo/<string:id_conteudo>
@app.put('/conteudo/<string:id_conteudo>')
def atualizar_conteudo(id_conteudo):

    dados = request.json

    for conteudo in conteudos.values():
        if conteudo["id"] == id_conteudo:
           conteudo.update(dados)
           return jsonify({"conteudo atualizado": conteudo}), 200
        
    return jsonify({"erro": "Notícia não encontrada"}), 404


if __name__ == '__main__':
    app.run(debug=True) 
    

  

        

        


        

        
  
    
    
   






