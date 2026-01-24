
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from flask import jsonify, request

import uuid

from db import db
from models.conteudo import ConteudoModel
from schemas.conteudo import ConteudoSchema


conteudo_blp = Blueprint(
    "Conteudo",
    __name__,
    description="Operações de conteúdo"
)

conteudos = {}


@conteudo_blp.route('/conteudo')
class Conteudo(MethodView):

    @conteudo_blp.response(200)
    def get(self):
        return jsonify({"Conteudos": list(conteudos.values())}), 200

    @conteudo_blp.arguments(ConteudoSchema)
    @conteudo_blp.response(201)
    def post(self, conteudo_dado):

        conteudo_id = uuid.uuid4().hex
        conteudo_novo = {**conteudo_dado, "id": conteudo_id}

        conteudos[conteudo_id] = conteudo_novo
        return conteudo_novo
@conteudo_blp.route('/conteudo/<string:id_conteudo>')
class ConteudoId(MethodView):

    @conteudo_blp.response(200)
    def get(self, id_conteudo):
        try:
            return jsonify(conteudos[id_conteudo])
        except KeyError:
            abort(404, message="Conteúdo não encontrado")

    @conteudo_blp.arguments(ConteudoSchema)
    @conteudo_blp.response(200)
    def put(self, dado, id_conteudo):

        for conteudo in conteudos.values():
            if conteudo["id"] == id_conteudo:
                conteudo.update(dado)
                return jsonify({"conteudo atualizado": conteudo}), 200

        abort(404, message="Conteúdo não encontrado")

    @conteudo_blp.response(200)
    def delete(self, id_conteudo):
        try:
            conteudos.pop(id_conteudo)
            return jsonify({"message": "Conteúdo removido com sucesso"})
        except KeyError:
            abort(404, message="Conteúdo não encontrado")

    @conteudo_blp.arguments(ConteudoSchema)
    @conteudo_blp.response(200)
    def patch(self, dados_conteudo, id_conteudo):

        if id_conteudo not in conteudos:
            abort(404, message="Conteúdo não encontrado")

        if not isinstance(dados_conteudo, dict) or len(dados_conteudo) == 0:
            abort(
                400,
                message="Dados inválidos, nenhum campo enviado para atualização"
            )

        if "id" in dados_conteudo and dados_conteudo["id"] != id_conteudo:
            abort(
                400,
                message="Operação não permitida, não é permitido atualizar o id do conteúdo"
            )

        dados_conteudo.pop("id", None)
        conteudos[id_conteudo].update(dados_conteudo)

        return jsonify({"conteudo atualizado": conteudos[id_conteudo]}), 200
