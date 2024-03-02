"""
Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros.
A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em
metros cúbicos.
"""

M = float(input('Digite o volume em metros cúbicos m³: '))
L = 1000 * M

print(f'{M}m³ equivalem a {L:.0f}l.')
