"""
Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em
km/h e M em m/s.
"""

K = float(input('Digite a velocidade em km/h (quilômetros por hora) que deseja converter para m/s (metros por segundo): '))
M: float = K / 3.6

print(f'{K} em m/s são {M}')
