
from marshmallow import Schema, fields

from schemas.plain import PlainEstoqueSchemas, PlainItemSchemas, PlainNoticiaSchemas


class NoticiaSchema(PlainNoticiaSchemas):
    itens = fields.List(fields.Nested(PlainItemSchemas()), dump_only=True)
    


class NoticiaSchemaUpdate(Schema): 
    departamento = fields.Str(required=False)
   