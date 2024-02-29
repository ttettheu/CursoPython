"""
Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, onde que
ele recebeu um aumento de 25%
"""

salario = float(input('Digite o valor do salário: '))
aumento = (salario * 25) / 100

print(f'O salário com aumento de 25% é R${salario + aumento:.2f}')
