# SQL

Esta pasta armazenará as consultas SQL usadas para responder perguntas de negócio.

Exemplos de consultas futuras:

- Receita por mês
- Pedidos por estado
- Categorias com maior faturamento
- Percentual de entregas atrasadas
- Relação entre atraso e avaliação do cliente

## Arquivos

- `business_questions.sql`: consultas SQL principais do projeto.

## Banco local

O banco SQLite é criado pelo script:

```text
src/create_sqlite_database.py
```

Depois de executar o script, o banco fica em:

```text
data/database/olist_analytics.sqlite
```

O arquivo `.sqlite` não é versionado no GitHub, mas pode ser recriado a partir de `data/processed/orders_analytics.csv`.
