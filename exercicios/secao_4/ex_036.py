"""
Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindo circular é calculado por meio da seguinte fórmula: V = π * raio² * altura, onde π = 3.141592.
"""

altura = float(input('Digite a altura: '))
raio = float(input('Digite o raio: '))
volume = 3.141592 * raio ** 2 * altura

print(f'O volume do cilindro é {volume}')
