
from flask_smorest import Blueprint, abort
from flask.views import MethodView
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models.noticia import NoticiaModel
from schemas.noticia import NoticiaSchema, NoticiaSchemaUpdate


noticia_blp = Blueprint(
    "Noticias",
    __name__,
    description="Operações relacionadas a notícias e conteúdos"
)


@noticia_blp.route("/noticias")
class Noticias(MethodView):

    @noticia_blp.response(200, NoticiaSchema(many=True))
    def get(self):
        return NoticiaModel.query.all()

    @noticia_blp.arguments(NoticiaSchema)
    @noticia_blp.response(201, NoticiaSchema)
    def post(self, noticia_dados):
        nova_noticia = NoticiaModel(**noticia_dados)

        try:
            db.session.add(nova_noticia)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message="Título e conteúdo são obrigatórios")

        return nova_noticia

@noticia_blp.route("/noticias/<string:id_noticia>")
class NoticiaId(MethodView):

    @noticia_blp.response(200, NoticiaSchema)
    def get(self, id_noticia):
        noticia = NoticiaModel.query.get(id_noticia)

        if not noticia:
            abort(404, message="Notícia não encontrada")

        return noticia

    @noticia_blp.arguments(NoticiaSchema)
    @noticia_blp.response(200, NoticiaSchema)
    def put(self, dados_novos, id_noticia):
        noticia = NoticiaModel.query.get(id_noticia)

        if not noticia:
            abort(404, message="Notícia não encontrada")

        noticia.conteudo = dados_novos["conteudo"]
        noticia.titulo = dados_novos["titulo"]

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message="Erro ao atualizar a notícia")

        return noticia

    @noticia_blp.arguments(NoticiaSchemaUpdate)
    @noticia_blp.response(200, NoticiaSchema)
    def patch(self, dados_noticia, id_noticia):
        noticia = NoticiaModel.query.get(id_noticia)

        if not noticia:
            abort(404, message="Notícia não encontrada")

        if "titulo" in dados_noticia:
            noticia.titulo = dados_noticia["titulo"]

        if "conteudo" in dados_noticia:
            noticia.conteudo = dados_noticia["conteudo"]

        try:
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
            abort(400, message="Erro ao atualizar a notícia")

        return noticia

    @noticia_blp.response(200)
    def delete(self, id_noticia):
        noticia = NoticiaModel.query.get_or_404(id_noticia)

        try:
            db.session.delete(noticia)
            db.session.commit()
            return {"message": "Notícia removida com sucesso"}, 200
        except IntegrityError:
            abort(
                400,
                message="Não foi possível excluir a notícia"
            )
