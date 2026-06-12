# Testes-com-Pytest
Mini desafio da Semana 3 do Bootcamp AWS AI FDE Driven Quality Engineering da Compass UOL. Projeto de automação de testes de API com Python, Pytest e Requests para validação dos endpoints de Usuários da ServeRest. 

Utilizei o Pycharm para a realização do desafio e tentei imitar o escopo do projeto passado em aula, copiando o nome dos diretórios e pastas.

Testes realizados:
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
Retorno:

### Teste 3

```

```
### Teste 3

```

```
### Teste 3

```

```
### Teste 3

```

```
### Teste 3

```

```
### Teste 3

```

```
