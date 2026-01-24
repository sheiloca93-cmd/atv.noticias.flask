
from marshmallow import fields, Schema

class PlainItemSchemas(Schema):
    id = fields.Str(dump_only=True)
    noticia = fields.Str(required=True)
    titulo_id = fields.Str(required=True)
    conteudo = fields.Str(required=True)


class PlainNoticiaSchemas(Schema):
    id = fields.Str(dump_only=True)
    conteudo = fields.Str(required=True)