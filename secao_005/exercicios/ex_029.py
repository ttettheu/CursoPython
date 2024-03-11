"""
Faça uma prova de matemática para crianças que estão aprendendo a somar números
inteiros menores do que 100. Escolha números aleatórios entre 1 a 100, e mostre na
tela a pergunta: qual é a soma de 'a + b', onde a e b são os números aleatórios. Peça a
resposta. Faça cinco perguntas ao aluno, e mostre para ele as perguntas e as respostas
corretas, além de quantas vezes o aluno acertou.
"""
import random

acertos = 0

for i in range(5):
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    soma = a + b
    resposta = int(input(f'Pegunta {i+1}: Qual é a soma de {a} + {b}? '))
    if resposta == soma:
        print('Resposta correta!')
        acertos += 1
    else:
        print(f'Resposta incorreta! A resposta correta era: {soma}')
print(f'Você acertou {acertos} perguntas de 5.')
