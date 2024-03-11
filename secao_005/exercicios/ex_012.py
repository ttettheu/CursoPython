"""
Ler um número inteiro. Se o número lido for negativo, escreva a mensagem 'Número
inválido'. Se o número for positivo, calcular o logaritmo deste número.
"""

numero = int(input("Digite um número inteiro: "))
log = 0

if numero <= 0:
    print('Número inválido.')
else:
    while numero > 1:
        log += 1
        numero /= 10
    print(f'O logaritmo de {numero} é {log}')

# Sei que existe a biblioteca math que pode fazer isso rapidinho, mas esse exercício corresponde
# a seção 5 e, até o momento não foi ensinado, acho que o professor quer que eu bata cabeça.
# O bom é que me força a pensar e entender os conceitos.