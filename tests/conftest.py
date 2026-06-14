"""
Utilização do fixture para organização e teste.
"""

import pytest
from src.api.usuarios_client import UsuariosClient # Cliente
from src.api.login_client import LoginClient # Login
from src.helpers.data_factory import gerar_usuario

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
