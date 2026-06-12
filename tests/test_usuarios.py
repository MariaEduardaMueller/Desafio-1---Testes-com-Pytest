'''
Testes feitos:
1. Validar cadastro de usuário
2. Cadastro com email repetido
3. Cadastro de usuário sem email
4. Cadastro sem passar variável de nome

5. Contagem de usuários

6. Busca de usuário específico por ID
7. Busca de usuário que não existe por ID

8. Atualizar usuário
9. Atualizar usuário inexistente

10. Excluir usuário existente
11. Excluir usuário inexistente
'''
from src.helpers.data_factory import gerar_usuario

# Cadastro -------------------------------------------
# Validar cadastro de usuário
def test_cadastro_usuario(client, novo_usuario):
    response = client.cadastrar_usuario(novo_usuario)
    body = response.json()
    assert response.status_code == 201
    assert body["message"] == "Cadastro realizado com sucesso"
    client.excluir_usuario(body["_id"])

# Cadastro sem passar variável de nome
def test_cadastro_usuario_sem_nome(client, novo_usuario):
    del novo_usuario["nome"]
    response = client.cadastrar_usuario(novo_usuario)
    body = response.json()
    assert response.status_code == 400
    assert "nome" in body
    assert body["nome"] == "nome é obrigatório"

# Cadastro de usuário sem email
def test_cadastro_sem_email(client, novo_usuario):
    del novo_usuario["email"]
    response = client.cadastrar_usuario(novo_usuario)
    assert response.status_code == 400

# Cadastro com email repetido
def test_cadastro_email_repetido(client, usuario_criado):
    _, payload = usuario_criado
    response = client.cadastrar_usuario(payload)
    assert response.status_code == 400


# Listagem de usuários -------------------------------------------
# Listar contagem de usuários para validação
def test_listar_usuarios(client):
    response = client.listar_usuarios()
    assert response.status_code == 200
    body = response.json()
    print("Quantidade:", body.get("quantidade"))
    print("Total na lista:", len(body.get("usuarios", [])))
    assert "usuarios" in response.json()


# Busca por ID -------------------------------------------
# Busca de usuário específico
def test_busca_usuario(client, usuario_criado):
    usuario_id, _ = usuario_criado
    response = client.buscar_usuario(usuario_id)
    assert response.status_code == 200
    assert response.json()["_id"] == usuario_id

# Busca de usuário que não existe
def test_busca_usuario_inexistente(client):
    response = client.buscar_usuario("id_invalido")
    assert response.status_code == 400


# Atualização de usuário -------------------------------------------
# Atualizar usuário
def test_atualiza_usuario(client, usuario_criado):
    usuario_id, _ = usuario_criado
    payload = gerar_usuario()
    response = client.atualizar_usuario(usuario_id,payload)
    assert response.status_code == 200

# Atualizar usuário inexistente
def test_atualiza_usuario_inexistente(client):
    id_inexistente = "id_que_nao_existe"
    payload = gerar_usuario()
    response = client.atualizar_usuario(id_inexistente, payload)
    body = response.json()
    assert response.status_code == 201
    assert body["message"] == "Cadastro realizado com sucesso"
    assert "_id" in body
    assert isinstance(body["_id"], str)
    client.excluir_usuario(body["_id"])


# Exclusão -------------------------------------------
# Excluir usuário
def test_excluir_usuario(client):
    payload = gerar_usuario()
    cadastro = client.cadastrar_usuario(payload)
    usuario_id = cadastro.json()["_id"]
    response = client.excluir_usuario(usuario_id)
    assert response.status_code == 200

# Excluir usuário inexistente
def test_excluir_usuario_inexistente(client):
    id_inexistente = "id_que_nao_existe"
    response = client.excluir_usuario(id_inexistente)
    assert response.status_code == 200
    body = response.json()
    assert "message" in body

