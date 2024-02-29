"""
Leia uma distância em milhas e apresente-a convertida em quilômetros.
A fórmula de conversão é: K = 1.61 * M, sendo K a distância em quilômetros e M em milhas.
"""

M = float(input('Digite a distância em milhas: '))
K = 1.61 * M

print(f'{M} milhas são {K} km')
