"""
Um produto vai sofrer aumento conforme a tabela abaixo. Leia o preço antigo,
calcule e escreva o preço novo, e escreva uma mensagem em função do preço novo
(conforme a segunda tabela).

    |     PREÇO ANTIGO     | PERCENTUAL DE AUMENTO |
    |      até R$ 50       |          5%           |
    | entre R$ 50 e R$ 100 |         10%           |
    |   acima de R$ 100    |         15%           |

    | PREÇO NOVO                        |  MENSAGEM  |
    | até R$ 80                         |   Barato   |
    | entre R$ 80 e R$ 120 (inclusive)  |   Normal   |
    | entre R$ 120 e R$ 200 (inclusive) |    Caro    |
    | acima de R$ 200                   | Muito caro |

"""

precoAntigo = float(input('Digite o preço antigo: '))

if precoAntigo <= 50:
    precoNovo = precoAntigo + precoAntigo * 0.05
elif precoAntigo <= 100:
    precoNovo = precoAntigo + precoAntigo * 0.1
else:
    precoNovo = precoAntigo + precoAntigo * 0.15

if precoNovo <= 80:
    mensagem = 'Barato'
elif precoNovo <= 120:
    mensagem = 'Normal'
elif precoNovo <= 200:
    mensagem = 'Caro'
else:
    mensagem = 'Muito Caro'

print(f'Preço novo: R${precoNovo:.2f} - {mensagem}')
