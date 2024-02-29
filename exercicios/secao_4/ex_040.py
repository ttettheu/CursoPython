"""
Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.
"""

dias_trabalhados = int(input('Quantos dias trabalhados? '))
imposto = (dias_trabalhados * 8) / 100

print(f'''
Diária: R$ 30,00
Dias Trabalhados: {dias_trabalhados}
Total Bruto: R$ {dias_trabalhados * 30:.2f}
Impostos (8%): R$ {imposto:.2f}
Toral Líquido: R$ {(dias_trabalhados * 30 - imposto):.2f}
''')
