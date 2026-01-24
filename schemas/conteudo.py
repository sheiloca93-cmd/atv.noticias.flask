
from marshmallow import Schema, fields
from schemas.plain import PlainItemSchemas

class ItemSchema(PlainItemSchemas):
	noticia_id = fields.Str(required=True)


class ItemSchemaUpdate(Schema):
	id = fields.Str(dump_only=True)
	noticia = fields.Str(required=False)
	titulo_id = fields.Str(required=False)
	conteudo = fields.Str(required=False)
	noticia_id = fields.Str(required=False)