from jsonschema import validate

# Para os testes de login
def validar_schema_login(body):
    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "string"},
            "authorization": {"type": "string"}
        },
        "required": [
            "message",
            "authorization"
        ]
    }
    validate(instance=body, schema=schema)

# Para os testes de usuários
def validar_schema_usuario(body):
    schema = {
        "type": "object",
        "properties": {
            "_id": {"type": "string"},
            "nome": {"type": "string"},
            "email": {"type": "string"},
            "password": {"type": "string"},
            "administrador": {"type": "string"}
        },
        "required": [
            "_id",
            "nome",
            "email",
            "password",
            "administrador"
        ]}
    validate(instance=body, schema=schema)

# Para os testes de produto
def validar_schema_produto(body):
    schema = {
        "type": "object",
        "properties": {
            "_id": {"type": "string"},
            "nome": {"type": "string"},
            "preco": {"type": "number"},
            "descricao": {"type": "string"},
            "quantidade": {"type": "number"}
        },
        "required": [
            "_id",
            "nome",
            "preco",
            "descricao",
            "quantidade"
        ]
    }
    validate(instance=body, schema=schema)
