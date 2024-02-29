"""
Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin.
A fórmula de conversão é: K = C + 273,15, sendo C a temperatura em Celsius
e K a temperatura em Kelvin.
"""

C = float(input('Digite a temperatura em ºC: '))
K = C + 273.15

print(f'{C}ºF são {K:.2f}ºC')
