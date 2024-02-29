"""
Leia um valor em real e a cotação do dólar. Em seguida, imrpima o valor correspondente
em dólares.
"""

real = float(input('Digite o valor em R$ (apenas números): '))
dolar = real / 4.98

print(f'R$ {real} equivalem a U$ {dolar:.2f}')
