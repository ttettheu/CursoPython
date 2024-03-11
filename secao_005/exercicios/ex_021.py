"""
Escreva o menu de opções abaixo. Leia a opção do usuário e execute a operação escolhida.
Escreva uma mensagem de erro se a opção for inválida.
    Escolha a opção:
    1 - Soma de 2 números.
    2 - Diferença entre 2 números (maior pelo menor).
    3 - Produto entre 2 números.
    4 - Divisão entre 2 números (o denominador não pode ser zero).
    Opção
"""

print('''
1 - Soma de 2 números.
2 - Diferença entre 2 números (maior pelo menor).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser zero).
''')
opcao = int(input('Escolha uma opção: '))
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))

if opcao == 1:
    print(f'Resultado: {num1 + num2}')
elif opcao == 2:
    print(f'Resultado: {abs(num1 - num2)}')  # Digita no terminal help(abs). Ele retorna o valor absoluto do argumento.
elif opcao == 3:
    print(f'Resultado: {num1 * num2}')
elif opcao == 4:
    if num2 != 0:
        print(f'Resultado: {num1 / num2}')
    else:
        print('O denominador não pode ser zero.')
else:
    print('Opção inválida. Por favor, escolha uma opção válida.')
