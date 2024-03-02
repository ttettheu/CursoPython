"""
Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros.
A fórmula de conversão é: C = P * 2.54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.
"""

P = float(input('Digite o valor de comprimento em polegadas: '))
C = P * 2.54

print(f'{P} pol equivalem a {C} cm.')
