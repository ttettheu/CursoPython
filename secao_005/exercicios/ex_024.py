"""
Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma taxa diferente
de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Faça um programa em que o usuário entre com
o valor e o estado destino do proguto e o programa retorne o preço final do produto acrescido do imposto
do estado em que ele será vendido. Se o estado digitado for inválido, mostrar uma mensagem de erro.
"""

valor = float(input('Digite o valor: '))
estado = int(input('''Escolha um estado:
1 - MG 7%\n2 - SP 12%\n3 - RJ 15%\n4 - MS 8%\n'''))

if estado == 1:
    print(f'Preço final: {valor + (valor * 7 / 100)}')
elif estado == 2:
    print(f'Preço final: {valor + (valor * 12 / 100)}')
elif estado == 3:
    print(f'Preço final: {valor + (valor * 15 / 100)}')
elif estado == 4:
    print(f'Preço final: {valor + (valor * 8 / 100)}')
else:
    print('Digite uma opção válida.')
