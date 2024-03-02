"""
Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C / 2,54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""

C = float(input('Digite o valor em centímetros: '))
P = C / 2.54

print(f'{C} cm equivalem a {P} pol.')
