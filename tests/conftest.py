"""
Utilização do fixture para organização e teste.
Achei bem prático para garantir que tudo o que for criado durante o teste seja excluído.
"""
import pytest
from src.api.usuarios_client import UsuariosClient
from src.helpers.data_factory import gerar_usuario

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
