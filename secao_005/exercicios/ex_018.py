"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas
(as básicas, por exemplo). O usuário escolhe uma das opções e o seu programa então pede
dois valores numéricos e realiza a operação, mostrando o resultado e saindo.
"""

escolha = int(input(f'''
ESCOLHA UMA OPÇÃO
Soma...........(1)
Subtração......(2)
Multiplicação..(3)
Divisão........(4)
'''))

valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

match escolha:
    case 1:
        print(f'A soma de {valor1} + {valor2} = {valor1 + valor2}')
    case 2:
        print(f'A subtração de {valor1} - {valor2} = {valor1 - valor2}')
    case 3:
        print(f'A multiplicação de {valor1} * {valor2} = {valor1 * valor2}')
    case 4:
        print(f'A divisão de {valor1} / {valor2} = {valor1 / valor2}')
    case _:
        print(f'Escolha uma opção válida (apenas números).')
