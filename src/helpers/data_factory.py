import uuid

# Para os testes de usuários
def gerar_usuario():
    identificador = uuid.uuid4().hex[:8]
    return {
        "nome": f"NomeAleatorio{identificador}",
        "email": f"nomealeatorio{identificador}@teste.com",
        "password": "123456",
        "administrador": "true"}

# Para os testes de produto
def gerar_produto():
    identificador = uuid.uuid4().hex[:8]
    return {
        "nome": f"Produto {identificador}",
        "preco": 100,
        "descricao": "Produto teste",
        "quantidade": 10}
