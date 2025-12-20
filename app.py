
from flask import Flask, jsonify, request

app = Flask(__name__)

noticias = [
    {
      "id": 1, 
        "nome": "Conteúdo da notícia 1"
    },
    {
      "id": 2,
        "nome": "Conteúdo da notícia 2"
    },
    {
      "id": 3,
        "nome": "Conteúdo da notícia 3"
    }
]

@app.get('/noticias')
def get_noticias():
    return jsonify({"Noticias": noticias})

@app.get('/noticia/<int:id>')
def get_noticia_by_id(id):
  
  @app.get('/noticia')
  def get_noticia():
     name = request.args.get('nome')


  for noticia in noticias:
        if noticia["nome"] == name:
           
         if noticias["id"] == id:
            return jsonify(noticia), 200
        
  return jsonify({"erro": "Notícia não encontrada"}), 404


@app.post('/noticia')
def add_noticia():
    nova_noticia = request.get_json()
    noticia = {
        "id": len(noticias) + 1,
        "nome": nova_noticia["nome"]
    }
    

    noticias.append(noticia)
    return jsonify(noticia), 201






if __name__ == '__main__':
    app.run(debug=True)




        

        


        

        
  
    
    
   






