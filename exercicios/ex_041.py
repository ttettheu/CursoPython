"""
Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas
trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre
o valor calculado.
"""

valor_hora = float(input('Qual o valor da hora de trabalho (R$)? '))
horas_trabalhadas = float(input('Quantas horas o funcionário trabalho no mês? '))
total_bruto = valor_hora * horas_trabalhadas
acrescimo = total_bruto * 10 / 100

print(f'''
Valor da Hora: R$ {valor_hora:.2f}
Horas Trabalhadas: R$ {horas_trabalhadas:.2f}
Total Bruto: R$ {total_bruto:.2f}
Acrescimo (10%): R$ {acrescimo:.2f}
Valor Líquido: R$ {total_bruto + acrescimo:.2f}
''')
