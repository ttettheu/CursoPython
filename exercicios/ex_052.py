"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-
porcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido.
"""

print('Digite os valores que cada um apostou:')
heitor = float(input('Heitor: '))
uriel = float(input('Uriel: '))
matheus = float(input('Matheus: '))
aposta = (heitor + uriel + matheus)
print(f'Total apostado: {aposta}')

print('\nDigite o valor do Prêmio:')
premio = float(input('Prêmio: '))

heitorGanha = (((heitor * aposta) / 100) * premio) / 100
urielGanha = (((uriel * aposta) / 100) * premio) / 100
matheusGanha = (((matheus * aposta) / 100) * premio) / 100

print(f'''
Valores proporcionais a aposta de cada ganhador:

Heitor ganhou R$ {heitorGanha:.2f}
Uriel ganhou R$ {urielGanha:.2f}
Matheus ganhou R$ {matheusGanha:.2f} 
''')