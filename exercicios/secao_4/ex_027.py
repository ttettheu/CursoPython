"""
Leia um valor de área em hectares e apresente-o convertido em metros quadrados m².
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a
área em hectares
"""

H = float(input('Digite o valor da área em hectares: '))
M = H * 10000
print(f'{H}ha equivalem a {M:.0f}m².')
