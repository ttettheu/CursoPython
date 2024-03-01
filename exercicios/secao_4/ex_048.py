"""
Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""

numero = int(input('Digite um valor em segundos: '))

print(f'''
Horas: {numero / 3600:.2f}
Minutos: {numero / 60:.2f}
Segundos: {numero}
''')
