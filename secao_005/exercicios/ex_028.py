"""
Faça um programa que leia três números inteiros positivos e efetue o cálculo de uma das
seguintes médias de acordo com um valor numérico digitado pelo usuário:

    (a) Geométrica: ³√x * y * z
    (b) Ponderada: x + 2 * y + 3 * z / 6
    (c) Harmônica: 1 / 1/x + 1/y + 1/z
    (d) Aritmética: x + y + z / 3
    
"""

x = int(input('Digite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

escolha = input('''
(a) Geométrica: ³√x * y * z
(b) Ponderada: x + 2 * y + 3 * z / 6
(c) Harmônica: 1 / 1/x + 1/y + 1/z
(d) Aritmética: x + y + z / 3

Escolha uma opção de calculo: ''').lower()

if escolha == 'a':
    resultado = (x * y * z) ** (1/3)
elif escolha == 'b':
    resultado = (x + 2 * y + 3 * z) / 6
elif escolha == 'c':
    resultado = 1 / ((1/x) + (1/y) + (1/z))
elif escolha == 'd':
    resultado = (x + y + z) / 3
else:
    print('Escolha uma opção válida.')

print(f'O resultado da média escolhida é: {resultado}')
