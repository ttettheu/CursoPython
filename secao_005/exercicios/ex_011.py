"""
Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a
soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor
8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a
mensagem 'Número inválido'.
"""

numero = int(input('Digite um número: ')) # Entrada de um número Inteiro
strNumero = str(numero) # Cast de interiro para String
soma = 0

for i in strNumero:
    soma += int(i)
print(soma)

"""
Cara, o que eu fiz aqui, acho que foi uma gambiarra kkk, mas deu certo!
Talvez tenha algo mais fácil, onde não precise fazer o cast de interio
para string mas, se tem ainda não aprendi.
"""
