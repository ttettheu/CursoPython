"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida dever ser, obrigatoriamente, um
valor entre 0,0 e 10,0, onde caso a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina.
"""

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

if nota1 <= 0 or nota1 >= 10 and nota2 <= 0 or nota2 >= 10:
    print(f'Nota não válida, digite as notas entre 0 e 10,00')
else:
    media = (nota1 + nota2) / 2
    print(f'Sua média é {media}')
