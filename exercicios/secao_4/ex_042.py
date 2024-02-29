"""
Recebe o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base.
"""

salario_base = float(input('Digite o Salário-Base do funcionário: '))
gratificacao = (salario_base * 5) / 100
imposto = (salario_base * 7) / 100
salario_liquido = salario_base + gratificacao - imposto

print(f'''
Salário-Base: R$ {salario_base:.2f}
Gratificação: + R$ {gratificacao:.2f}
Imposto: - R$ {imposto:.2f}
Salário Líquido: R$ {salario_liquido:.2f}
''')
