"""
Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
    A = (basemaior + basemenor) * altura / 2
Lembre-se a base maior e base menor devem ser número maiores que zero.
"""
print('Área de um Trapézio')
baseMaior = float(input('Digite o valor da base maior: '))
baseMenor = float(input('Digite o valor da base menor: '))
altura = float(input('Digite o valor da altura: '))
A = (baseMaior + baseMenor) * altura / 2

if baseMaior > 0 and baseMenor > 0:
    print(f'A área do trapézio é {A}')
else:
    print(f'A base maior e a base menor devem ser números maiores que zero.')
