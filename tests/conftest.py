"""
Utilização do fixture para organização e teste.
"""

import pytest
from src.api.usuarios_client import UsuariosClient # Cliente
from src.api.login_client import LoginClient # Login
from src.api.produtos_client import ProdutosClient # Produtos
from src.helpers.data_factory import gerar_usuario, gerar_produto

#Para os testes de login
@pytest.fixture
def login_client():
    return LoginClient()

# Para os testes de usuário:
@pytest.fixture
def client():
    return UsuariosClient()
@pytest.fixture
def novo_usuario():
    return gerar_usuario()
@pytest.fixture
def usuario_criado(client):
    payload = gerar_usuario()
    response = client.cadastrar_usuario(payload)
    usuario_id = response.json()["_id"]
    yield usuario_id, payload
    client.excluir_usuario(usuario_id)

# Para os testes de produto
@pytest.fixture
def token_admin(login_client, usuario_criado):
    _, payload = usuario_criado
    login = login_client.login(
        {
            "email": payload["email"],
            "password": payload["password"]
        })
    return login.json()["authorization"]


@pytest.fixture
def produto_criado(produtos_client, token_admin):
    payload = gerar_produto()
    response = produtos_client.cadastrar_produto(payload, token_admin)
    produto_id = response.json()["_id"]
    yield produto_id, payload
    produtos_client.excluir_produto(produto_id, token_admin)
