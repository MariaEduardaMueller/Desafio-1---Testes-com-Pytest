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
- [Report de Bugs, Erros e Inconsistências Encontradas](#report-de-bugs-erros-e-inconsistências-encontradas)

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

### Taxa de cobertura
Foi utilizado como base o artigo: https://medium.com/revista-dtar/como-verificar-a-cobertura-de-testes-da-api-rest-9e2f745564b e a atual documentação da ServeRest para fazer a contagem de endpoints e métodos (GET, POST, PUT, DELETE) da API. 

<img width="645" height="485" alt="image" src="https://github.com/user-attachments/assets/dcd26115-46b0-4385-990b-4547e97f1314" />

## Path Coverage (input):

(5 / 9) x 100 = 55,55% dos testes de path estão cobertos.

<img width="800" height="601" alt="taxacaminhocoberturanovo" src="https://github.com/user-attachments/assets/06c88fad-c61d-49d1-9238-4d08dfe01040" />


## Operator Coverage (input):

(11/16) x 100 = 68,75% de cobertura funcional da API.

<img width="800" height="601" alt="taxacoberturanovo" src="https://github.com/user-attachments/assets/177b6eec-8486-4355-ab9c-ba229e06edf1" />


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
### Teste 11 - Excluir produto com ID inválido
```
def test_excluir_produto_id_invalido(produtos_client, token_admin):
    response = produtos_client.excluir_produto("123456", token_admin)
    body = response.json()
    assert response.status_code == 400
    assert "id" in body
```

### Teste 11 - Excluir produto inexistente
```
def test_excluir_produto_inexistente(produtos_client, token_admin):
        response = produtos_client.excluir_produto("1234567111711111", token_admin)
        print(response.status_code)
        print(response.json())
```

## Report de Bugs, Erros e Inconsistências Encontradas

Além de registrar os defeitos encontrados na seção Issues do GitHub, optei por documentá-los também neste relatório para facilitar a análise e rastreabilidade dos problemas identificados durante os testes automatizados da API.

### Bug #1 – Endpoint /produtos/{id} | Atualização de produto inexistente cria um novo produto

**Severidade:** Alta
**Prioridade:** Alta

**Endpoint:** `PUT /produtos/{id}`

#### Descrição

Ao realizar uma requisição de atualização (`PUT`) para um produto utilizando um ID válido, porém inexistente na base de dados, a API cria um novo produto em vez de retornar uma mensagem informando que o recurso não foi encontrado.

#### Passos para reproduzir

1. Gerar um payload válido de produto.
2. Executar um `PUT /produtos/{id}` utilizando um ID com 16 caracteres alfanuméricos que não exista na base.
3. Analisar a resposta retornada pela API.

#### Resultado esperado

A API deveria retornar uma resposta indicando que o produto não foi encontrado, por exemplo:

```json
{
  "message": "Produto não encontrado"
}
```

com status HTTP `404 Not Found` (ou outro status definido pela especificação da API).

#### Resultado obtido

A API retorna:

```json
{
  "message": "Cadastro realizado com sucesso",
  "_id": "..."
}
```

com status HTTP `201 Created`, criando um novo produto.

#### Impacto

Esse comportamento pode gerar registros indevidos na base de dados, causar inconsistências nos dados da aplicação e induzir consumidores da API a acreditar que a atualização foi realizada com sucesso, quando na verdade um novo recurso foi criado.

---

### Inconsistência #1 – Endpoint /produtos/{id} | Tratamento inconsistente para IDs inexistentes

**Severidade:** Média
**Prioridade:** Média

**Endpoints:** `PUT /produtos/{id}` e `DELETE /produtos/{id}`

#### Descrição

A API apresenta comportamentos distintos ao receber IDs inválidos e IDs válidos, porém inexistentes.

#### Cenário 1 – ID inválido

**Requisição:**

Utilizar um ID fora do padrão esperado.

**Resultado obtido:**

```json
{
  "id": "id deve ter exatamente 16 caracteres alfanuméricos"
}
```

**Status HTTP:** `400 Bad Request`

#### Cenário 2 – ID válido, porém inexistente (PUT)

**Requisição:**

Utilizar um ID com 16 caracteres alfanuméricos que não exista na base.

**Resultado obtido:**

```json
{
  "message": "Cadastro realizado com sucesso"
}
```

**Status HTTP:** `201 Created`

#### Cenário 3 – ID válido, porém inexistente (DELETE)

**Requisição:**

Utilizar um ID com 16 caracteres alfanuméricos que não exista na base.

**Resultado obtido:**

```json
{
  "message": "Nenhum registro excluído"
}
```

**Status HTTP:** `200 OK`

#### Impacto

Embora a validação de formato esteja correta, o tratamento de recursos inexistentes não segue um comportamento uniforme entre os endpoints testados, dificultando a implementação de tratamentos de erro por parte dos consumidores da API.

---

### Observação #1 – Endpoint /login | Login com campos vazios retorna 400

**Severidade:** Informativa
**Prioridade:** Baixa

**Endpoint:** `POST /login`

#### Descrição

Ao realizar login enviando os campos de e-mail e senha vazios, a API retorna:

```json
{
  "email": "email não pode ficar em branco",
  "password": "password não pode ficar em branco"
}
```

**Status HTTP:** `400 Bad Request`

#### Observação

Esse comportamento não caracteriza necessariamente um defeito, pois a API está validando corretamente os campos obrigatórios antes de executar a autenticação.

No entanto, foi registrado por representar um comportamento diferente do observado em cenários de credenciais inválidas, nos quais a API retorna status `401 Unauthorized`.

#### Resultado esperado

Comportamento sujeito à regra de negócio definida pela equipe responsável pela API.

---

## Resumo Executivo

Durante a execução dos testes automatizados foram identificados:

* **1 bug de alta severidade** relacionado ao endpoint de atualização de produtos.
* **1 inconsistência funcional de média severidade** relacionada ao tratamento de recursos inexistentes.
* **1 observação de comportamento** referente à validação de campos obrigatórios no processo de autenticação.

Os resultados indicam que a API possui boa estabilidade nos fluxos principais testados, porém apresenta oportunidades de melhoria relacionadas à consistência das respostas e ao tratamento de operações realizadas sobre recursos inexistentes.

