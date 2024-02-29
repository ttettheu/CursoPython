"""
Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³.
A fórmula de conversão é: M = L / 1000, sendo L o volume em litros e M o volume em
metros cúbicos.
"""

L = float(input('Digite o valor de volume em litros: '))
M = L / 1000

print(f'{L}l equivalem a {M}m³.')
