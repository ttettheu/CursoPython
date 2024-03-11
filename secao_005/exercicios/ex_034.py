"""
Leia a nota e o número de faltas de um aluno, e escreva seu conceito. Conforme a
tabela abaixo, quando o aluno tem mais de 20 faltas ocorre uma redução de conceito.

    |     NOTA     | CONCEITO (ATÉ 20 FALTAS) | CONCEITO (MAIS DE 20 FALTAS) |
    | 9.0 até 10.0 |            A             |              B               |
    | 7.5 até 8.0  |            B             |              C               |
    | 5.0 até 7.4  |            C             |              D               |
    | 4.0 até 4.9  |            D             |              E               |
    | 0.0 até 3.0  |            E             |              E               |

"""

nota = float(input('Digite a nota: '))
faltas = int(input('Digite o número de faltas: '))

if nota >= 0:
    if nota >= 9 and nota <= 10:
        conceito = 'A'
    elif nota >= 7.5:
        cocneito = 'B'
    elif nota >= 5:
        cocneito = 'C'
    elif nota >= 4:
        cocneito = 'D'
    else:
        cocneito = 'E'
else:
    print('Digite uma nota válida. (Entre 1 e 10)')

if faltas >= 0:
    if faltas > 20:
        if nota >= 9 and nota <= 10:
            conceito = 'B'
        elif nota >= 7.5:
             cocneito = 'C'
        elif nota >= 5:
            cocneito = 'D'
        elif nota >= 4:
            cocneito = 'E'
    print(f'Nota: {nota} Faltas: {faltas} - Conceito: {conceito}')
