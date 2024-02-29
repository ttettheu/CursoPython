"""
Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora).
A fórmula de conversão é: K = M * 3,6, sendo K a velocidade em km/h e M em m/s.
"""

M = float(input('Digite a velocidade em m/s: '))
K: float = M * 3.6

print(f'{M}m/s são {K}km/h')
