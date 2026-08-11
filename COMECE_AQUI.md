# Comece Aqui

Este arquivo guia os primeiros passos do projeto.

## Onde estamos agora

A estrutura inicial do projeto já foi criada. Ainda não baixamos os dados e ainda não começamos a análise.

## Passo 1: Baixar os dados

1. Acesse o dataset da Olist no Kaggle:

   https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

2. Clique em **Download**.

3. Extraia o arquivo `.zip`.

4. Copie todos os arquivos `.csv` extraídos para esta pasta do projeto:

   ```text
   data/raw/
   ```

## Passo 2: Confirmar que os arquivos estão no lugar certo

Depois de copiar os arquivos, a pasta `data/raw/` deve conter arquivos parecidos com estes:

```text
olist_customers_dataset.csv
olist_geolocation_dataset.csv
olist_order_items_dataset.csv
olist_order_payments_dataset.csv
olist_order_reviews_dataset.csv
olist_orders_dataset.csv
olist_products_dataset.csv
olist_sellers_dataset.csv
product_category_name_translation.csv
```

## Passo 3: Próxima ação com a IA

Quando os arquivos estiverem em `data/raw/`, envie uma mensagem como:

```text
Já coloquei os dados na pasta data/raw. Pode continuar.
```

A partir daí, a próxima etapa será:

1. Verificar se todos os arquivos esperados existem.
2. Ler as primeiras linhas de cada CSV.
3. Criar um resumo das tabelas.
4. Montar o primeiro notebook de análise exploratória.
5. Criar a base SQLite para praticar SQL.

## Importante

Você não precisa decorar comandos agora. Eu vou te orientar um passo por vez e explicar o motivo de cada ação.

