"""
Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno
com tela.
"""

c = float(input('Digite o comprimento: '))
l = float(input('Digite a largura: '))
p = float(input('Digite o valor da tela: '))
custo = (c * 2) + (l * 2) * p

print(f'O custo para um perímetro de {c * 2 + l * 2}m é R$ {custo}.')
