"""
Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:

NúmeroLido = 123
NúmeroGerado = 321
"""

numeroLido: int = input('Digite um número (de 100 a 999): ')
numeroGerado: str = numeroLido[:3]

print(f'''
Número Lido = {numeroLido}
Número Gerado = {numeroGerado[::-1]}
''')

"""
Queria muito ter colocado uma limitação no input, pelas aulas não encontrei essa opção e,
nem sei se é possível. Mas por enquanto é isso.
"""