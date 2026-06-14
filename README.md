# Desafio Final - Testes com Pytest
Desafio do Bootcamp AWS AI FDE Driven Quality Engineering da Compass UOL. Projeto de automação de testes de API com Python, Pytest e Requests para validação dos endpoints de Usuários, Login e Produtos da ServeRest (Base URL: https://compassuol.serverest.dev/)
[incluir plano de testes]

## Sumário
- [Escopo do Projeto](#escopo-do-projeto)
- [Como Executar](#como-executar)
- [Taxa de Cobertura](#taxa-de-cobertura)
- [Testes Realizados](#testes-realizados)
  - [/login](#testes-de-login)
  - [/usuarios](#testes-de-usuários)
  - [/produtos](#testes-de-produtos)
- [Report de Bugs, Erros e Inconsistências Encontradas](#bugs-encontrados)

## Escopo do Projeto

<img width="450" height="511" alt="image" src="https://github.com/user-attachments/assets/b62b208c-ae52-4e3b-ac26-9e0c8e741720" />


## Como Executar
Baixe o repositório e, depois de extrair os arquivos do .zip, o adicione no editor de código desejado:
<img width="584" height="230" alt="image" src="https://github.com/user-attachments/assets/d8530021-e154-4c0e-a65b-90f4b2a8ed28" />


Instale as bibliotecas necessárias pelas configurações da IDE ou pelo terminal utilizando o `requirements.txt` como base:
```
pytest
requests
jsonschema
```
<br> </br>
Caso não tenha o Python instalado utilize o terminal para rodar o comando:
```
winget install Python.Python
```
Ou baixe o Python pelo site: https://www.python.org/downloads/

<br> </br>

### Testes realizados:

# Testes de Login
### Teste 1 - Teste de Login válido (com validação de Schema)
```
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

```
### Teste 2 - Login com senha inválida
```
def test_login_senha_incorreta(login_client, usuario_criado):
    _, payload = usuario_criado
    response = login_client.login(
        {
            "email": payload["email"],
            "password": "senha_errada"
        })
    assert response.status_code == 401
```
### Teste 3 - Login com email inexistente
```
def test_login_email_inexistente(login_client):
    response = login_client.login(
        {
            "email": "emaialeatorio@email.com",
            "password": "1234567"
        })
    assert response.status_code == 401
```

### Teste 4 - Login com campos vazios
```
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
```

# Testes de Usuários
## Testes de Cadastro
### Teste 1 - Validar cadastro de usuário
```
def test_cadastro_usuario(client, novo_usuario):
    response = client.cadastrar_usuario(novo_usuario)
    body = response.json()
    assert response.status_code == 201
    assert body["message"] == "Cadastro realizado com sucesso"
    client.excluir_usuario(body["_id"])
```

### Teste 2 - Cadastro sem passar variável de nome
```
def test_cadastro_usuario_sem_nome(client, novo_usuario):
    del novo_usuario["nome"]
    response = client.cadastrar_usuario(novo_usuario)
    body = response.json()
    assert response.status_code == 400
    assert "nome" in body
    assert body["nome"] == "nome é obrigatório"
```

### Teste 3 - Cadastro de usuário sem passar email
```
def test_cadastro_sem_email(client, novo_usuario):
    del novo_usuario["email"]
    response = client.cadastrar_usuario(novo_usuario)
    assert response.status_code == 400
```

### Teste 4 - Cadastro com email repetido
```
def test_cadastro_email_repetido(client, usuario_criado):
    _, payload = usuario_criado
    response = client.cadastrar_usuario(payload)
    assert response.status_code == 400

```

## Listagem de usuários
### Teste 5 -  Listar contagem de usuários para validação
```
def test_listar_usuarios(client):
    response = client.listar_usuarios()
    assert response.status_code == 200
    body = response.json()
    print("Qtd.:", body.get("quantidade"))
    print("Qtd. Total:", len(body.get("usuarios", [])))
    assert "usuarios" in response.json()

```
Exemplo de retorno esperado:

<img width="817" height="139" alt="image" src="https://github.com/user-attachments/assets/e8b61dce-785b-42de-8787-53c8444dd445" />


## Busca por ID
### Teste 6 - Busca de usuário específico (com validação de Schema)
```
def test_busca_usuario(client, usuario_criado):
    usuario_id, _ = usuario_criado
    response = client.buscar_usuario(usuario_id)
    body = response.json()
    assert response.status_code == 200
    assert body["_id"] == usuario_id
    validar_schema_usuario(body)
```

### Teste 7 - Busca de usuário que não existe
```
def test_busca_usuario_inexistente(client):
    response = client.buscar_usuario("id_invalido")
    assert response.status_code == 400

```
## Atualização de usuário
### Teste 8 - Atualizar usuário
```
def test_atualiza_usuario(client, usuario_criado):
    usuario_id, _ = usuario_criado
    payload = gerar_usuario()
    response = client.atualizar_usuario(usuario_id,payload)
    assert response.status_code == 200
```

### Teste 9 - Atualizar usuário inexistente
```
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
```

## Exclusão de usuário
### Teste 10 - Excluir usuário
```
def test_excluir_usuario(client):
    payload = gerar_usuario()
    cadastro = client.cadastrar_usuario(payload)
    usuario_id = cadastro.json()["_id"]
    response = client.excluir_usuario(usuario_id)
    assert response.status_code == 200

```

### Teste 11 - Excluir usuário inexistente
```
def test_excluir_usuario_inexistente(client):
    id_inexistente = "id_que_nao_existe"
    response = client.excluir_usuario(id_inexistente)
    assert response.status_code == 200
    body = response.json()
    assert "message" in body
```

# Testes de Produtos
### Teste 1 - Listar produtos

```
def test_listar_produtos(produtos_client):
    response = produtos_client.listar_produtos()
    assert response.status_code == 200
    body = response.json()
    assert "produtos" in body
```
### Teste 2 - Busca por ID (com validação de Schema)
```
def test_busca_produto(produtos_client):
    response = produtos_client.listar_produtos()
    produto_id = response.json()["produtos"][0]["_id"]
    busca = produtos_client.buscar_produto(produto_id)
    body = busca.json()
    assert busca.status_code == 200
    assert body["_id"] == produto_id
    validar_schema_produto(body)
```
### Teste 3 - Busca produto inexistente
```
def test_busca_produto_inexistente(produtos_client):
    response = produtos_client.buscar_produto("id_inexistente")
    assert response.status_code == 400
```
### Teste 4 - Cadastro com token
```
def test_cadastrar_produto(produtos_client, token_admin):
    payload = gerar_produto()
    response = produtos_client.cadastrar_produto(payload, token_admin)
    assert response.status_code == 201
    produto_id = response.json()["_id"]
    produtos_client.excluir_produto(produto_id, token_admin)
```
### Teste 5 - Cadastro sem token
```
def test_cadastrar_produto_sem_token(produtos_client):
    payload = gerar_produto()
    response = produtos_client.cadastrar_produto(payload, "")
    assert response.status_code == 401
```
### Teste 6 - Cadastro de produto com nome duplicado
```
def test_cadastrar_produto_nome_repetido(produtos_client, token_admin):
    payload = gerar_produto()
    cadastro = produtos_client.cadastrar_produto(payload, token_admin)
    produto_id = cadastro.json()["_id"]
    response = produtos_client.cadastrar_produto(payload, token_admin)
    assert response.status_code == 400
    produtos_client.excluir_produto(produto_id, token_admin)
```
### Teste 7 - Atualizar produto
```
def test_atualizar_produto(produtos_client, token_admin, produto_criado):
    produto_id, _ = produto_criado
    novo_payload = gerar_produto()
    response = produtos_client.atualizar_produto(produto_id, novo_payload, token_admin)
    assert response.status_code == 200
```
### Teste 8 - Atualizar produto inexistente
```
def test_atualizar_produto_inexistente(produtos_client, token_admin):
    payload = gerar_produto()
    response = produtos_client.atualizar_produto("1234567891111111", payload, token_admin)
    assert response.status_code == 201
    produto_id = response.json()["_id"]
    produtos_client.excluir_produto( produto_id, token_admin)
```
### Teste 9 - Excluir produto
```
def test_excluir_produto(produtos_client, token_admin):
    payload = gerar_produto()
    cadastro = produtos_client.cadastrar_produto(payload, token_admin)
    produto_id = cadastro.json()["_id"]
    response = produtos_client.excluir_produto(produto_id, token_admin)
    assert response.status_code == 200
```
### Teste 10 - Excluir produto inexistente
```
def test_excluir_produto_inexistente(produtos_client, token_admin):
    response = produtos_client.excluir_produto("123456", token_admin)
    body = response.json()
    assert response.status_code == 400
    assert "id" in body
```
