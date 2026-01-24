from flask import Flask
from flask_smorest import Api
from resources.noticia import noticia_blp
from resources.conteudo import conteudo_blp
from models import LojaModel, NoticiaModel, ConteudoModel


def create_app():
    app = Flask(__name__)

from db import db
from models import NoticiaModel, ConteudoModel

import os


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Notícias API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
    

    app.config["SQLALCHEMY_DATABASE_URI"] = (
        db_url or os.getenv("DATABASE_URL", "sqlite:///data.db")
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    api = Api(app)

    # 🔗 Registrando os blueprints
    api.register_blueprint(noticia_blp)
    api.register_blueprint(conteudo_blp)

    with app.app_context():
        db.create_all()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
