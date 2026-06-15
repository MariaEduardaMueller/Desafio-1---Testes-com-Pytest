'''
Testes na base /login

Testes feitos:
1. Teste de Login válido (com validação de Schema)
2. Login com senha inválida
3. Login com email inexistente
4. Login com campos vázios

'''
from src.helpers.schemas import validar_schema_login

# Teste de login válido (com validação de Schema)
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

# Login com senha inválida
def test_login_senha_incorreta(login_client, usuario_criado):
    _, payload = usuario_criado
    response = login_client.login(
        {
            "email": payload["email"],
            "password": "senha_errada"
        })
    assert response.status_code == 401

# Login com email inexistente
def test_login_email_inexistente(login_client):
    response = login_client.login(
        {
            "email": "emaialeatorio@email.com",
            "password": "1234567"
        })
    assert response.status_code == 401

# Login com campos vázios
def test_login_campos_vazios(login_client):
    response = login_client.login(
        {
            "email": "",
            "password": ""
        })
    body = response.json()
    assert response.status_code == 400
    assert body["email"] == "email não pode ficar em branco"
    assert body["password"] == "password não pode ficar em branco"
