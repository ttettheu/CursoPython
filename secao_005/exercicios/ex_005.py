"""
Faça um programa que receba um número inteiro e verifique se este número é par ou
ímpar.
"""

numero = int(input('Digite um número inteiro: '))

if (numero % 2) == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é impar.')
