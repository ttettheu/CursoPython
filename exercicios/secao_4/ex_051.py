"""
Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua
distância de origem (0,0).
"""

x = float(input('Digite o valor de x: '))
y = float(input('Digite o valor de y: '))
resultado = ((x ** 2) + (y ** 2) ** (1 / 2))

print(f'A distância de origem é: {resultado}.')
