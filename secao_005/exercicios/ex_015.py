"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante.
"""

numero = int(input('Digite um número inteiro entre 1 e 7: '))

if numero == 1:
    print('Domindo')
elif numero == 2:
    print('Segunda-feira')
elif numero == 3:
    print('Terça-feira')
elif numero == 4:
    print('Quarta-feira')
elif numero == 5:
    print('Quinta-feira')
elif numero == 6:
    print('Sexta-feira')
elif numero == 7:
    print('Sábado')
else:
    print(f'O {numero} não é um número entre 1 e 7, tente novamente!')

# Não usei switch, não foi ensinado na aula da seção 5. E o programa funciona mesmo sem ele.
