import uuid

def gerar_usuario():
    identificador = uuid.uuid4().hex[:8]
    return {
        "nome": f"NomeAleatorio{identificador}",
        "email": f"nomealeatorio{identificador}@teste.com",
        "password": "123456",
        "administrador": "true"}
