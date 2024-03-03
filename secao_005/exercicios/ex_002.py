"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido.
"""

numero = float(input('Digite um número: '))

if numero > 0:
    print(f'{numero} é positivo e sua raiz quadrada é {numero ** (1/2)}')
else:
    print(f'{numero} é inválido.')
