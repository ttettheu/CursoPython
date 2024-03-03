"""
Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,
assim como a diferença existem entre ambos.
"""

numero1 = int(input('Digite um número inteiro: '))
numero2 = int(input('Digite outro número inteiro: '))

if numero1 > numero2:
    print(f'O maior é {numero1} e a diferença é {numero1 - numero2}')
else:
    print(f'O maior é {numero2} e a diferença é {numero2 - numero1}')
