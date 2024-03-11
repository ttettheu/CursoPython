"""
Faça um programa que receba a altura e o peso de uma pessoa. Conforme a tabela
a seguir, verifique e mostra qual a classificação dessa pessoa.

    |     Altura     |                          Peso                    |
    |                | Até 60 | Entre 60 e 90 (Inclusive) | Acima de 90 |
    | Menor que 1,20 |    A   |             D             |      G      |
    | De 1,20 a 1,70 |    B   |             E             |      H      |
    | Maior que 1,70 |    C   |             F             |      I      |

"""

altura = float(input('Digite a altura: '))
peso = float(input('Digite o peso: '))

if altura < 1.20:
    if peso <= 60:
        classificacao = 'A'
    elif peso <= 90:
        classificacao = 'D'
    else:
        classificacao = 'G'
elif altura <= 1.70:
    if peso <= 60:
        classificacao = 'B'
    elif peso <= 90:
        classificacao = 'E'
    else:
        classificacao = 'H'
else:
    if peso <= 60:
        classificacao = 'C'
    elif peso <= 90:
        classificacao = 'F'
    else:
        classificacao = 'I'
print(f'Sua classificação é: {classificacao}')
