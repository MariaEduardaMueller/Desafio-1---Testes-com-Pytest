# Desafio 1 - Testes com Pytest
Mini desafio da Semana 3 do Bootcamp AWS AI FDE Driven Quality Engineering da Compass UOL. Projeto de automação de testes de API com Python, Pytest e Requests para validação dos endpoints de Usuários da ServeRest (Base URL: https://compassuol.serverest.dev/usuarios)

Utilizei o Pycharm para a realização do desafio e tentei imitar o escopo do projeto passado em aula, copiando o nome dos diretórios e pastas.
Nisso criei pytest.fixture no ` conftest.py ` , o ` pytest.ini ` (também testei passando os parâmetros `-s -v` no próprio Pycharm sem ser por código), criei classes no `usuarios_client.py` para facilitar na criação de testes e também para eu melhorar meus conhecimentos.


## Testes realizados
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
### Teste 6 - Busca de usuário específico
```
def test_busca_usuario(client, usuario_criado):
    usuario_id, _ = usuario_criado
    response = client.buscar_usuario(usuario_id)
    assert response.status_code == 200
    assert response.json()["_id"] == usuario_id
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
