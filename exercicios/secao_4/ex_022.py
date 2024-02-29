"""
Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula
de conversão é: M = 0,91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
"""

J = float(input('Digite o valor do comprimento em jardas: '))
print(f'{J}yd equivalem a {J * 0.91}m')
