"""
Leia um ângulo em graus e apresente-o convertido em radianos.
A fórmula de conversão é: R = G * π/180, sendo G o ângulo em graus e R em radianos e π = 3.14.
"""

G = float(input('Digite o ângulo em graus: '))
R: float = G * 3.14 / 180

print(f'{G}º são {R} radianos')
