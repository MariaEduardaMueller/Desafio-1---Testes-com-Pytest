'''
Testes na base /login
'''
from src.helpers.schemas import validar_schema_login

# Teste de Login Válido (com validação de Schema)
def test_login(login_client, usuario_criado):
    _, payload = usuario_criado
    response = login_client.login(
        {
            "email": payload["email"],
            "password": payload["password"]
        }
    )
    body = response.json()
    assert response.status_code == 200
    validar_schema_login(body)


# Senha inválida
def test_login_senha_incorreta(login_client, usuario_criado):
    _, payload = usuario_criado
    response = login_client.login(
        {
            "email": payload["email"],
            "password": "senha_errada"
        })
    assert response.status_code == 401

# Email Inexistente
def test_login_email_inexistente(login_client):
    response = login_client.login(
        {
            "email": "naoexiste@email.com",
            "password": "123456"
        })
    assert response.status_code == 401

# Login com campos vázios
def test_login_campos_vazios(login_client):
    response = login_client.login(
        {
            "email": "",
            "password": ""
        })
    assert response.status_code == 401

