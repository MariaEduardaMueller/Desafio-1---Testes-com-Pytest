import uuid

def gerar_usuario():
    identificador = uuid.uuid4().hex[:8]
    return {
        "nome": f"Maria Teste {identificador}",
        "email": f"maria{identificador}@teste.com",
        "password": "123456",
        "administrador": "true"}
