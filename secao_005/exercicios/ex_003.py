"""
Leia um número real. Se o número for positivo imprima a raiz quadrada. Do contrário,
imprima o número ao quadrado.
"""

numero = float(input('Digite um número real: '))

if numero > 0:
    print(f'A raiz quadrade de {numero} é {numero ** (1/2)}')
else:
    print(f'O número {numero} ao quadrado é {numero ** 2}')
