"""
Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
    - O número digitado ao quadrado
    - A raiz quadrada do número digitado
"""

numero = float(input('Digite um número: '))

if numero > 0:
    print(f'{numero} ao quadrado é igual a {numero ** 2} e a sua raiz é {numero ** (1/2)}')
