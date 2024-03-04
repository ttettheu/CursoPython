"""
Faça um program que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
    - Homenes: (72.7 * h) - 58
    - Mulheres: (62.1 * h) - 44.7
"""

altura = float(input('Digite a altura: '))
sexo = input('Digite seu sexo: ')

if sexo.lower() == 'homem':
    pesoIdeal = (72.7 * altura) - 58
    print(f'Seu peso ideal é {pesoIdeal}')
elif sexo.lower() == 'mulher':
    pesoIdeal = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é {pesoIdeal}')
