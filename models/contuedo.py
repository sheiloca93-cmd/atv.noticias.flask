from db import db

class ConteudoModel(db.Model):
    __tablename__ = 'conteudos'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=True)
    conteudo = db.Column(db.Text, nullable=False, unique=False)
    titulo_id = db.Column(db.String, db.ForeignKey('noticias.id'), unique=False, nullable=True)


    noticias = db.relationship('NoticiaModel', back_populates='conteudo', lazy='dynamic')
    