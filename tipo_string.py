"""
Tipo string

Em Python, um dado é considerado um tipo string sempre que:

- Estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''

nome = 'ttettheu'
print(nome)
print(type(nome))

nome = "ttettheu"
print(nome)
print(type(nome))

nome = '''Matheus \nAlcântara'''
print(nome)
print(type(nome))

nome = "Matheus \" Alcântara"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:7]) # Slice de string

print(nome[8:17]) # Slice de string

# [     0,         1     ]
# ['Matheus', 'Alcântara']
print(nome.split()[0])

print(nome.split()[1])
"""
# Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

# [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9,  10,  11,  12,  13,  14,  15,  16, ]
# ['M', 'a', 't', 'h', 'e', 'u', 's', ' ', 'A', 'l', 'c', 'â', 'n', 't', 'a', 'r', 'a',]
nome = 'Matheus Alcântara'

"""
[::-1] -> Comece do primeiro elemento, vá até o último e inverta
"""
print(nome[::-1]) # Inversão de String Pythônico

print(nome.replace('M', 'E'))

print(type(nome))

texto = 'socorram me subino onibus em marrocos' # Palíndromo
print(texto)

print(texto[::-1])

nome = 'hannah' # Palíndromo

print(nome[::-1])
