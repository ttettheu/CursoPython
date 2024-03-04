"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima: 'Empréstimo não concedido', caso
contrário imprima: 'Emprestimo concedido.'.
"""

salario = float(input('Digite o salário: '))
prestacao = float(input('Digite o valor da prestação: '))
porcentagem = (salario * 20) / 100

if prestacao > porcentagem:
    print('Esmprestimo não concedido.')
else:
    print('Emprestimo concedido.')
