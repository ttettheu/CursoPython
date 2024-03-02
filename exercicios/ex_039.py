"""
A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:
    - O primeiro ganhador receberá 46%;
    - O segundo receberá 32%;
    - O terceiro receberá o restante:
Calcule e imprima a quantia ganhada por cada um dos ganhadores.
"""

premio = 780_000
primeiro = (premio * 46) / 100
segundo = (premio * 32) / 100
terceiro = premio * (100 - 46 - 32) / 100

print(f'''
Um prêmio de R$ 780.000,00 dividido para três ganhadores é:
Primeiro (46%): R$ {primeiro:.2f}
Segundo (32%): R$ {segundo:.2f}
Terceiro ({100 - 46 - 32}%): R$ {terceiro:.2f} 
''')
