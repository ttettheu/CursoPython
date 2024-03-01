"""
Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
ASCII para resolver o problema.
"""

entrada = input('Digite algo para converter de maiúsculo para minúsculo: ')

print(f'{entrada} >>> {entrada.casefold()}')
