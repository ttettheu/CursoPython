"""
Leia uma data e determine se ela é válida. Ou seja, verifique se o mês está entre 1 e 12,
e se o dia existe naquele mês. Nota que Fevereiro tem 29 dias em anos bissextos, e 28 dias
em anos não bissextos.
"""

dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
maxDia = None

"""Percebi ter uma mensagem de erro por conta de ser uma variável local.
Então, declarei para sumir a mensagem no PyCharm"""

if mes < 1 or mes > 12:
    print('Data inválida.')

if mes in [1, 3, 5, 7, 8, 10, 12]:
    maxDia = 31
elif mes in [4, 6, 9, 11]:
    maxDia = 30
elif mes == 2:
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        maxDia = 29
    else:
        maxDia = 28

if dia < 1 or dia > maxDia:
    print('Data inválida.')
else:
    print('Data válida.')
