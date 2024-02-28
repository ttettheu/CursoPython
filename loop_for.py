"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma destas estruturas

C ou Java

for(int i = 0; i < limitador; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Gkke University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range[1, 10]

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando em uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)

range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não

for numero in range(1, 10):
    print(numero)

Enumerate:

((0, 'G'), ('e'), ('e'), ('k'), (' '), ('U'), ('n')...)

for indice, letra enumerate(nome):
    print(nome[numero])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

OBS: Quando não precisamos de um valor podemos descartá-los utilizando um underline (_)

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes este loop deve rodar? '))
soma = 0

for n in range(1, qtd + 1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

Tabela de Emoji Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
"""

# Original: U+2665
# Modificado: U0002665

for _ in range(3):
    for num in range(1, 11):
        print('\U0002665' * num)
