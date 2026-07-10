# SIMPLEMOOC

Plataforma simples de MOOC (Massive Open Online Course) desenvolvida em **Python/Django**.

## Sobre

Sistema web para criação e gerenciamento de cursos online, com cadastro de alunos, cursos, aulas e fórum de dúvidas.

## Tecnologias

- Python 3
- Django
- SQLite (padrão)
- HTML/CSS

## Configuração

1. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente copiando `.env.example` para `.env` e preenchendo os valores.

4. Execute as migrations:

```bash
python manage.py migrate
```

5. Inicie o servidor:

```bash
python manage.py runserver
```

## Estrutura

- `simplemooc/` — Aplicação principal.
- `manage.py` — CLI do Django.
- `requirements.txt` — Dependências Python.
- `Procfile` — Configuração para deploy no Heroku.

## Próximos passos

- Atualizar para Django LTS mais recente.
- Substituir SQLite por PostgreSQL em produção.
- Adicionar testes automatizados.
