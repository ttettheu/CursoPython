"""
Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
"""

altura_degrau = float(input('Digite a altura do degrau (cm): '))
altura_desejada = float(input('Digite a altura que deseja alcançar (cm): '))

print(f'Você precisará subir {altura_desejada / altura_degrau:.0f} degraus para alcançar a altura de {altura_desejada:.0f}')
