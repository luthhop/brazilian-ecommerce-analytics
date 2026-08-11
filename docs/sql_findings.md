# Conclusões da Análise SQL

Este documento resume os principais achados das consultas SQL executadas no notebook `04_sql_business_analysis.ipynb`.

## 1. Status dos pedidos

A maior parte dos pedidos está no status `delivered`, com 96.478 pedidos entregues.

| Status | Pedidos |
| --- | ---: |
| delivered | 96.478 |
| shipped | 1.107 |
| canceled | 625 |
| unavailable | 609 |
| invoiced | 314 |
| processing | 301 |

## 2. Categorias com maior receita

As categorias que mais contribuíram para receita de produtos foram:

| Categoria | Pedidos | Receita |
| --- | ---: | ---: |
| health_beauty | 8.613 | 1.233.813,10 |
| watches_gifts | 5.478 | 1.167.152,18 |
| bed_bath_table | 9.184 | 1.024.243,76 |
| sports_leisure | 7.493 | 954.525,89 |
| computers_accessories | 6.512 | 888.593,98 |

## 3. Estados com maior faturamento

O faturamento está fortemente concentrado no Sudeste, especialmente em São Paulo.

| Estado | Pedidos | Receita |
| --- | ---: | ---: |
| SP | 40.501 | 5.067.633,16 |
| RJ | 12.350 | 1.759.651,13 |
| MG | 11.354 | 1.552.481,83 |
| RS | 5.345 | 728.897,47 |
| PR | 4.923 | 666.063,51 |

## 4. Atraso e avaliação

Pedidos atrasados apresentam nota média consideravelmente menor.

| Entrega atrasada | Pedidos | Nota média | Atraso médio |
| --- | ---: | ---: | ---: |
| Não | 89.443 | 4,29 | -13,51 dias |
| Sim | 6.381 | 2,27 | 10,52 dias |

Interpretação: pedidos entregues no prazo ou antes do prazo têm avaliação média próxima de 4,3. Pedidos atrasados têm avaliação média próxima de 2,3, indicando forte relação entre desempenho logístico e satisfação do cliente.

## 5. Categorias com maior taxa de atraso

Considerando apenas categorias com pelo menos 500 pedidos entregues:

| Categoria | Pedidos entregues | Taxa de atraso | Nota média |
| --- | ---: | ---: | ---: |
| baby | 2.761 | 8,11% | 4,12 |
| office_furniture | 1.251 | 8,07% | 3,65 |
| electronics | 2.502 | 7,67% | 4,13 |
| musical_instruments | 608 | 7,57% | 4,24 |
| health_beauty | 8.613 | 7,54% | 4,23 |

## 6. Tipos de pagamento

Cartão de crédito é o meio de pagamento dominante.

| Pagamento | Pedidos | Valor pago | Parcelas médias |
| --- | ---: | ---: | ---: |
| credit_card | 72.825 | 12.102.206,16 | 3,55 |
| boleto | 19.191 | 2.769.932,58 | 1,00 |
| voucher | 2.977 | 341.951,91 | 1,15 |
| debit_card | 1.484 | 208.371,12 | 1,00 |

## 7. Estados com maior tempo médio de entrega

Os maiores tempos médios de entrega aparecem em estados da região Norte e Nordeste.

| Estado | Pedidos entregues | Tempo médio de entrega | Atraso médio | Nota média |
| --- | ---: | ---: | ---: | ---: |
| RR | 41 | 29,39 dias | -17,29 dias | 3,90 |
| AP | 67 | 27,19 dias | -19,69 dias | 4,24 |
| AM | 145 | 26,43 dias | -19,57 dias | 4,24 |
| AL | 397 | 24,54 dias | -8,71 dias | 3,85 |
| PA | 946 | 23,77 dias | -14,07 dias | 3,91 |

## Insight principal

O principal achado até aqui é que atraso na entrega está associado a uma queda relevante na satisfação do cliente. A nota média cai de 4,29 em pedidos não atrasados para 2,27 em pedidos atrasados.

Esse insight pode orientar recomendações de negócio voltadas à melhoria logística, priorização de categorias com maior taxa de atraso e monitoramento regional do tempo de entrega.

