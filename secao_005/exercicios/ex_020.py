"""
Dados três valores, A, B, C, verificar se eles podem ser valores dos lados de um triângulo e, se forem,
se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes conceitos:
    - O comprimento de cada lado de um triângulo com três lados iguais.
    - Chama-se equilátero o triângulo com três lados iguais.
    - Denomina-se isósceles o triângulo com o comprimento de dois lados iguais.
    - Recebe o nome de escaleno o triângulo com os três lados diferentes.
"""

a = float(input('Digite o valor do lado A: '))
b = float(input('Digite o valor do lado B: '))
c = float(input('Digite o valor do lado C: '))

if a == b == c:
    print('É um triângulo equilátero.')
elif a == b or a == c or b == c:
    print('É um triângulo isósceles.')
elif a != b and a != c and b != c:
    print('É um triângulo escaleno.')
