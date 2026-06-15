# Plano de Testes

## Objetivo

Validar o comportamento funcional dos endpoints da API ServeRest solicitados no desafio do Bootcamp AWS AI FDE DRIVEN QE, garantindo que as operações de autenticação, gerenciamento de usuários e gerenciamento de produtos retornem os resultados esperados para cenários positivos e negativos.

---

## Estratégia

### Tipo de teste

* Testes de API REST
* Testes funcionais
* Caixa preta (Black Box Testing)

### Camada de teste

* Camada de serviço (API)

### Ferramentas

* Python
* Pytest
* Requests
* JsonSchema

---

## Escopo

### Coberto

#### Login

* Autenticação de usuários
* Validação de credenciais
* Tratamento de credenciais inválidas

#### Usuários

* Cadastro de usuários
* Consulta de usuários
* Atualização de usuários
* Exclusão de usuários

#### Produtos

* Cadastro de produtos
* Consulta de produtos
* Atualização de produtos
* Exclusão de produtos

### Fora de Escopo

* Endpoint de Carrinhos
* Testes de performance
* Testes de carga
* Testes de estresse
* Testes de segurança
* Testes de acessibilidade
* Testes de interface gráfica (UI)

---

## Cenários Implementados

### POST /login

| ID     | Cenário                                |
| ------ | -------------------------------------- |
| LGN-01 | Realizar login com credenciais válidas |
| LGN-02 | Realizar login com senha incorreta     |
| LGN-03 | Realizar login com email inexistente   |
| LGN-04 | Realizar login com campos vazios       |

---

### GET /usuarios

| ID     | Cenário                                  |
| ------ | ---------------------------------------- |
| USR-01 | Listar usuários cadastrados              |
| USR-02 | Validar quantidade retornada na listagem |

### POST /usuarios

| ID     | Cenário                                      |
| ------ | -------------------------------------------- |
| USR-03 | Cadastrar usuário válido                     |
| USR-04 | Tentar cadastrar usuário com email duplicado |
| USR-05 | Tentar cadastrar usuário sem email           |
| USR-06 | Tentar cadastrar usuário sem nome            |

### GET /usuarios/{id}

| ID     | Cenário                         |
| ------ | ------------------------------- |
| USR-07 | Buscar usuário existente por ID |
| USR-08 | Buscar usuário inexistente      |

### PUT /usuarios/{id}

| ID     | Cenário                       |
| ------ | ----------------------------- |
| USR-09 | Atualizar usuário existente   |
| USR-10 | Atualizar usuário inexistente |

### DELETE /usuarios/{id}

| ID     | Cenário                     |
| ------ | --------------------------- |
| USR-11 | Excluir usuário existente   |
| USR-12 | Excluir usuário inexistente |

---

### GET /produtos

| ID     | Cenário                     |
| ------ | --------------------------- |
| PRD-01 | Listar produtos cadastrados |

### POST /produtos

| ID     | Cenário                                     |
| ------ | ------------------------------------------- |
| PRD-02 | Cadastrar produto com token válido          |
| PRD-03 | Tentar cadastrar produto sem token          |
| PRD-04 | Tentar cadastrar produto com nome duplicado |

### GET /produtos/{id}

| ID     | Cenário                         |
| ------ | ------------------------------- |
| PRD-05 | Buscar produto existente por ID |
| PRD-06 | Buscar produto inexistente      |

### PUT /produtos/{id}

| ID     | Cenário                       |
| ------ | ----------------------------- |
| PRD-07 | Atualizar produto existente   |
| PRD-08 | Atualizar produto inexistente |

### DELETE /produtos/{id}

| ID     | Cenário                     |
| ------ | --------------------------- |
| PRD-09 | Excluir produto existente   |
| PRD-10 | Excluir produto inexistente |

---

## Critérios de Qualidade

Um teste é considerado pronto quando:

* Possui objetivo claramente definido.
* É independente dos demais testes.
* Utiliza dados dinâmicos para evitar conflitos de execução.
* Possui asserts específicos e verificáveis.
* Valida o código de status HTTP esperado.
* Valida o conteúdo da resposta quando aplicável.
* Valida schemas JSON nos endpoints críticos.
* Realiza limpeza dos dados criados durante a execução (cleanup).
* Pode ser executado repetidamente sem interferir em execuções anteriores.

---

## Cobertura Funcional

### Recursos cobertos

* Login
* Usuários
* Produtos

### Recursos não cobertos

* Carrinhos

### Cobertura estimada

* Recursos cobertos: 3 de 4
* Cobertura funcional estimada: 75%
