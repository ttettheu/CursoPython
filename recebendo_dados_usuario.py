"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python String é tudo que estiver entre:
- Aspas simples
- Aspas duplas
- Aspas simples triplas
- Aspas duplas triplas

Exemplos:
- Aspas simples -> 'Maria Eduarda'
- Aspas duplas -> "Maria Eduarda"
- Aspas simples triplas -> '''Maria Eduarda'''
"""
# - Aspas duplas triplas -> """Maria Eduarda"""

# Entrada de dados
# print('Qual seu nome? ')
# nome = input() # Input -> Entrada

nome = input('Qual o seu nome? ')

# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

# print('Qual sua idade? ')
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento

# Saída de dados
# Exemplo de print 'antigo' 2.x
# print('A %s tem %s anos' % (nome, idade))

# Exemplo de print 'moderno' 3.x
# print('A {0} tem {0} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos')

"""
# int(idade) => cast

cast é a 'conversão' de um tipo de dado para outro.
"""
print(f'A {nome} nasceu em {2024 - idade}')