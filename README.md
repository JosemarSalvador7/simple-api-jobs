# API de vagas de emprego

Este projeto é uma API REST desenvolvida com Django e Django REST Framework para gerenciar vagas de emprego e competências associadas.

## Objetivo

A aplicação permite criar, listar, editar e remover:
- vagas de emprego
- competências disponíveis para associar às vagas

A estrutura foi organizada em dois apps principais:
- `jobs`: representa as vagas de emprego
- `skills`: representa as competências

## Funcionalidades principais

- CRUD completo para vagas (`jobs`)
- CRUD completo para competências (`skills`)
- Relação muitos-para-muitos entre vagas e competências
- Painel administrativo do Django disponível

## Tecnologias utilizadas

- Python 3.12+
- Django
- Django REST Framework
- SQLite (banco padrão para desenvolvimento)
- python-decouple
- drf-spectacular (dependência instalada, mas ainda sem documentação OpenAPI exposta)

## Estrutura do projeto

```text
core/           # configuração principal do projeto Django
jobs/           # app com os modelos, serializers, views e rotas das vagas
skills/         # app com os modelos, serializers, views e rotas das skills
migrations/     # migrações do banco de dados
manage.py       # utilitário de gerenciamento do Django
```

## Modelos principais

### Job
Campos:
- `title`: título da vaga
- `description`: descrição da vaga
- `salary`: salário da vaga
- `skills`: relação muitos-para-muitos com `Skill`

### Skill
Campos:
- `name`: nome da competência

## Pré-requisitos

- Python 3.12+
- pip
- virtualenv ou venv

## Instalação

1. Entre na pasta do projeto:
   ```bash
   cd /caminho/para/o/projeto
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Instale as dependências:
   ```bash
   pip install -e .
   ```

4. Crie um arquivo `.env` na raiz do projeto com as variáveis abaixo:
   ```env
   SECRET_KEY=sua-chave-secreta
   DEBUG=True
   ALLOWED_HOSTS=*
   ```

## Execução

Execute as migrações:
```bash
python manage.py migrate
```

Crie um usuário administrativo:
```bash
python manage.py createsuperuser
```

Inicie o servidor de desenvolvimento:
```bash
python manage.py runserver
```

A API ficará disponível em:
```text
http://127.0.0.1:8000/
```

O painel administrativo poderá ser acessado em:
```text
http://127.0.0.1:8000/admin/
```

## Endpoints da API

As rotas são montadas automaticamente com routers do DRF.

### Skills
- `GET /api/skills/` — lista todas as competências
- `POST /api/skills/` — cria uma nova competência
- `GET /api/skills/<id>/` — detalha uma competência
- `PUT /api/skills/<id>/` — atualiza uma competência
- `PATCH /api/skills/<id>/` — atualiza parcialmente uma competência
- `DELETE /api/skills/<id>/` — remove uma competência

### Jobs
- `GET /api/jobs/` — lista todas as vagas
- `POST /api/jobs/` — cria uma nova vaga
- `GET /api/jobs/<id>/` — detalha uma vaga
- `PUT /api/jobs/<id>/` — atualiza uma vaga
- `PATCH /api/jobs/<id>/` — atualiza parcialmente uma vaga
- `DELETE /api/jobs/<id>/` — remove uma vaga

## Exemplos de requisições

### Criar uma competência

```bash
curl -X POST http://127.0.0.1:8000/api/skills/ \
  -H "Content-Type: application/json" \
  -d '{"name": "Python"}'
```

### Criar uma vaga

```bash
curl -X POST http://127.0.0.1:8000/api/jobs/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Desenvolvedor Python",
    "description": "Vaga para desenvolver APIs com Django REST Framework.",
    "salary": "6500.00",
    "skills": [1, 2]
  }'
```

## Exemplo de payload para criar uma vaga

```json
{
  "title": "Desenvolvedor Python",
  "description": "Vaga para desenvolver APIs com Django Rest Framework.",
  "salary": "6500.00",
  "skills": [1, 2]
}
```

## Exemplo de payload para criar uma competência

```json
{
  "name": "Python"
}
```

## Observações importantes

- O campo `skills` em `Job` espera os IDs de competências já existentes.
- O valor de `salary` deve ser enviado como texto ou número no formato decimal compatível com o serializer.
- A API ainda não possui autenticação de usuários nem paginação configurada por padrão.

## Próximos passos

Possíveis melhorias para o projeto:
- adicionar autenticação de usuários
- implementar filtros e paginação
- criar testes automatizados
- documentar a API com Swagger/OpenAPI
