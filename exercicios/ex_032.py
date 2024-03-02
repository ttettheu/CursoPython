"""
Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de
seu dobro.
"""

numero = int(input('Digite um número: '))
sucessor_triplo = ((numero*3)+1)
antecessor_dobro = ((numero*2)-1)
soma = sucessor_triplo + antecessor_dobro

print(f'Sucessor do seu triplo: {sucessor_triplo}\nAntecessor do seu dobro: {antecessor_dobro}\nSoma: {soma}')
