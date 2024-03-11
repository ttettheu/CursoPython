"""
Leia a distância em Km e a quantidade de litros de gasolina consumidos por um carro
em um percurso, calcule o consumo em Km/l e escreva uma mensagem conforme a tabela abaixo:

    | CONSUMO   | (Km/l) | MENSAGEM         |
    | menor que |   8    | Venda o carro!   |
    | entre     | 8 e 14 | Econômico!       |
    | maior que |   12   | Super econômico! |

"""

distancia = float(input('Digite a distância em km: '))
litros = float(input('Digite a quantidade de litros de gasolina consumidos: '))

consumo = distancia / litros

if consumo < 8:
    print(f'Consumo: {consumo:.2f} Km/l - Venda o carro!')
elif consumo >= 8 and consumo <= 14:
    print(f'Consumo: {consumo:.2f} Km/l - Econômico!')
else:
    print(f'Consumo: {consumo:.2f} Km/l - Super economico')
