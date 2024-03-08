"""
Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante.
"""

numero = int(input('Digite um número inteiro entre 1 e 7: '))

match numero:
    case 1:
        print('Domindo')
    case 2:
        print('Segunda-feira')
    case 3:
        print('Terça-feira')
    case 4:
        print('Quarta-feira')
    case 5:
        print('Quinta-feira')
    case 6:
        print('Sexta-feira')
    case 7:
        print('Sábado')
    case _:
        print(f'{numero} não é um número entre 1 e 7, tente novamente!')

# Agora usei switch, não foi ensinado na aula da seção 5. Pesquisei e apliquei.
