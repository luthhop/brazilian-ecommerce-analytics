# Dicionário Inicial de Dados

Fonte: Brazilian E-Commerce Public Dataset by Olist.

Este documento registra a primeira leitura das tabelas brutas em `data/raw`.

## Tabelas

| Arquivo | Linhas | Colunas | Descrição inicial |
| --- | ---: | ---: | --- |
| `olist_customers_dataset.csv` | 99.441 | 5 | Clientes, localização e identificadores. |
| `olist_geolocation_dataset.csv` | 1.000.163 | 5 | Coordenadas geográficas por prefixo de CEP. |
| `olist_order_items_dataset.csv` | 112.650 | 7 | Itens dos pedidos, produtos, vendedores, preço e frete. |
| `olist_order_payments_dataset.csv` | 103.886 | 5 | Pagamentos, parcelas, tipo de pagamento e valor pago. |
| `olist_order_reviews_dataset.csv` | 99.224 | 7 | Avaliações dos pedidos, notas e comentários. |
| `olist_orders_dataset.csv` | 99.441 | 8 | Pedidos, status e datas do funil logístico. |
| `olist_products_dataset.csv` | 32.951 | 9 | Produtos, categorias e atributos físicos. |
| `olist_sellers_dataset.csv` | 3.095 | 4 | Vendedores e localização. |
| `product_category_name_translation.csv` | 71 | 2 | Tradução das categorias de produto para inglês. |

## Principais chaves

| Chave | Uso |
| --- | --- |
| `order_id` | Liga pedidos, itens, pagamentos e avaliações. |
| `customer_id` | Liga pedidos aos clientes. |
| `product_id` | Liga itens aos produtos. |
| `seller_id` | Liga itens aos vendedores. |
| `product_category_name` | Liga produtos à tabela de tradução de categorias. |

## Relações esperadas

```text
customers.customer_id -> orders.customer_id
orders.order_id -> order_items.order_id
orders.order_id -> order_payments.order_id
orders.order_id -> order_reviews.order_id
order_items.product_id -> products.product_id
order_items.seller_id -> sellers.seller_id
products.product_category_name -> product_category_name_translation.product_category_name
```

## Observações iniciais

- `olist_geolocation_dataset.csv` é a maior tabela do projeto.
- `olist_order_items_dataset.csv` tem mais linhas que `olist_orders_dataset.csv` porque um pedido pode ter mais de um item.
- `olist_order_payments_dataset.csv` também pode ter mais linhas que pedidos porque um pedido pode ter mais de um registro de pagamento.
- `product_category_name_translation.csv` é pequena e servirá como tabela auxiliar.

