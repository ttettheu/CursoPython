"""
Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
    - O total a pagar com desconto de 10%;
    - O valor de cada parcela, no parcelamento de 3x sem juros;
    - A comissão de vendedor, no caso da enda ser a vista (5% sobre o valor com desconto)
    - A comissão do vendedor, no caso de venda ser parcelada (5% sobre o valor total)
"""

valor_total = float(input('Valor total: '))
desconto = (valor_total * 10) / 100
valor_pagar = valor_total - desconto
comissao_avista = (desconto * 5) / 100
comissao_parcelado = (valor_total * 5) / 100

print(f'''
Valor da venda: R$ {valor_total:.2f}
Desconto (10%): R$ {desconto:.2f}

1x sem juros: R$ {valor_pagar:.2f}
2x sem juros: R$ {valor_pagar / 2:.2f}
3x sem juros: R$ {valor_pagar / 3:.2f}

Comissão a vista: R$ {comissao_avista:.2f}
Comissão parcelado: R$ {comissao_parcelado:.2f}
''')
