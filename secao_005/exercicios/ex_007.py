"""
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois
números forem iguais, imprima a mensagem 'Números iguais'.
"""

numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

if numero1 > numero2:
    print(f'O maior é o número {numero1}')
if numero1 == numero2:
    print(f'Números iguais')
else:
    print(f'O maior é o número {numero2}')
