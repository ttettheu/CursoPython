"""
Leia um ângulo em radianos e apresente-o convertido em graus.
A fórmula de conversão é: G = R * 180/π, sendo G o ângulo em graus e R em radianos e π = 3.14.
"""

R = float(input('Digite o ângulo em radianos: '))
G = R * 180 / 3.14

print(f'{R} radianos são {G} graus')
