"""
Faça um programa que receba três números e mostre-os em ordem crescente.
"""
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
numeros = [a, b, c]

print(f'Número em ordem crescente: {sorted(numeros)}')
