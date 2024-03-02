"""
Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação:
hipotenusa = √ a² + b². Faça um programa que receba os valores de a e b e calcule
o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""

a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
hipotenusa = (a ** 2 + b ** 2) ** (1 / 2)

print(f'''O valor da hipotenusa para
a = {a}
b = {b}
hipotenusa é {hipotenusa}''')
