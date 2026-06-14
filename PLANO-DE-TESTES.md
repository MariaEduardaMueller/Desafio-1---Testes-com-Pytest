# Plano de Testes

## Objetivo

Validar o comportamento dos endpoints de Usuários, Login e Produtos da API ServeRest solicidados no desafio do Bootcamp: AWS AI FDE DRIVEN QE.


## Estratégia

Tipo de teste:
- Testes de API REST
- Caixa preta
- Testes funcionais

Ferramentas:
- Python
- Pytest
- Requests


## Escopo

### Coberto

Usuários:
- Cadastro
- Consulta
- Atualização
- Exclusão

Login:
- Login válido
- Senha inválida
- Email inexistente
- Campos vazios

Produtos:
- Cadastro
- Consulta
- Atualização
- Exclusão

### Fora de escopo

- Performance
- Segurança
- Testes de carga

---

## Critérios de qualidade

- Assert específico
- Testes independentes
- Dados dinâmicos
- Cleanup quando necessário
