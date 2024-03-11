"""
Escreva um programa que, dada a idade de um nadador, classifique-o em uma das
seguintes categorias:

    | Categoria  |       Idade        |
    | Infantil A |       5 a 7        |
    | Intantil B |       8 a 10       |
    | Juvenil A  |      11 e 13       |
    | Juvenil B  |      14 e 17       |
    | Sênio      | maiores de 18 anos |

"""

idade = int(input('Digite a idade: '))

if idade >= 5 and idade <= 7:
    categoria = 'Infantil A'
elif idade >= 8 and idade <= 10:
    categoria = 'Infantil B'
elif idade >= 11 and idade <= 13:
    categoria = 'Juvenil A'
elif idade >= 14 and idade <= 17:
    categoria = 'Juvenil B'
elif idade >= 18:
    categoria = 'Sênior'

print(f'O nanador está na categoria: {categoria}')
