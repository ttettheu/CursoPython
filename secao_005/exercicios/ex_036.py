"""
Escreva um programa que, dado o valor da venda, imprima a comissão que deverá ser
paga ao vendedor. Para calcular a comissão, considere a tabela abaixo:

    |                   VENDA MENSAL                          |          COMISSÃO          |
    | Maior ou igual a R$ 100.000,00                          | R$ 700,00 + 16% das vendas |
    | Menor que R$ 100.000,00 e maior ou igual a R$ 80.000,00 | R$ 650,00 + 14% das vendas |
    | Menor que R$ 80.000,00 e maior ou igual a R$ 60.000,00  | R$ 600,00 + 14% das vendas |
    | Menor que R$ 60.000, 00 e maior ou igual a R$ 40.000,00 | R$ 550,00 + 14% das vendas |
    | Menor que R$ 40.000,00 e maior ou igual a R$ 20.000,00  | R$ 500,00 + 14% das vendas |
    | Menor que R$ 20.000,00                                  | R$ 400,00 + 14% das vendas |

"""

venda = float(input('Digite o valor da venda mensal: '))
comissao = None

if venda > 0:
    if venda < 20_000:
        comissao = 400 + 400 * 0.14
    elif venda < 40_000:
        comissao = 500 + 500 * 0.14
    elif venda < 60_000:
        comissao = 550 + 550 * 0.14
    elif venda < 80_000:
        comissao = 600 + 600 * 0.14
    elif venda < 100_000:
        comissao = 650 + 650 * 0.14
    elif venda >= 100_000:
        comissao = 700 + 700 * 0.16
    print(f'Você receberá uma comissão de {comissao}')
else:
    print(f'Digite o valor de venda válido.')
