'''
Testes da base /produtos
'''
from src.helpers.data_factory import gerar_produto
from src.helpers.schemas import validar_schema_produto

# Listar produtos
def test_listar_produtos(produtos_client):
    response = produtos_client.listar_produtos()
    assert response.status_code == 200
    body = response.json()
    assert "produtos" in body

# Busca por ID (com validação de Schema)
def test_busca_produto(produtos_client):
    response = produtos_client.listar_produtos()
    produto_id = response.json()["produtos"][0]["_id"]
    busca = produtos_client.buscar_produto(produto_id)
    body = busca.json()
    assert busca.status_code == 200
    assert body["_id"] == produto_id
    validar_schema_produto(body)

# Busca produto inexistente
def test_busca_produto_inexistente(produtos_client):
    response = produtos_client.buscar_produto("id_inexistente")
    assert response.status_code == 400

# Cadastro com token
def test_cadastrar_produto(produtos_client, token_admin):
    payload = gerar_produto()
    response = produtos_client.cadastrar_produto(payload, token_admin)
    assert response.status_code == 201

# Cadastro sem token
def test_cadastrar_produto_sem_token(produtos_client):
    payload = gerar_produto()
    response = produtos_client.cadastrar_produto(payload, "")
    assert response.status_code == 401


# Atualizar produto
def test_atualizar_produto(produtos_client, token_admin):
    payload = gerar_produto()
    cadastro = produtos_client.cadastrar_produto(payload, token_admin)
    produto_id = cadastro.json()["_id"]
    novo_payload = gerar_produto()
    response = produtos_client.atualizar_produto(produto_id, novo_payload, token_admin)
    assert response.status_code == 200

# Excluir produto
def test_excluir_produto(produtos_client, token_admin):
    payload = gerar_produto()
    cadastro = produtos_client.cadastrar_produto(payload, token_admin)
    produto_id = cadastro.json()["_id"]
    response = produtos_client.excluir_produto(produto_id, token_admin)
    assert response.status_code == 200

# Excluir teste inexistente
def test_excluir_produto_inexistente(produtos_client, token_admin):
    response = produtos_client.excluir_produto("id_inexistente", token_admin)
    assert response.status_code == 200

  
