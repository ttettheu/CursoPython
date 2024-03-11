"""
Escrever um programa que leia o código do produto escolhido do cardápio de uma lanchonete
e a quantidade. O programa deve calcular o valor a ser pago por aquele lanche.
Considere que a cada execução será somente calculado um pedido. O cardápio da lanchonete
segue o padrão abaixo:

     |  Especificação  | Código | Preço |
     | Cachorro Quente |  100   |  1.20 |
     | Bauru Simples   |  101   |  1.30 |
     | Bauru com Ovo   |  102   |  1.50 |
     | Hamburguer      |  103   |  1.20 |
     | Cheeseburguer   |  104   |  1.70 |
     | Suco            |  105   |  2.20 |
     | Refrigerante    |  106   |  1.0  |

"""
cardapio = {
    100: {'Especificação': 'Cachorro Quente', 'Preço': 1.20},
    101: {'Especificação': 'Bauru Simples', 'Preço': 1.30},
    102: {'Especificação': 'Bauru com Ovo', 'Preço': 1.50},
    103: {'Especificação': 'Hamburguer', 'Preço': 1.20},
    104: {'Especificação': 'Cheeseburguer', 'Preço': 1.70},
    105: {'Especificação': 'Suco', 'Preço': 2.20},
    106: {'Especificação': 'Refrigerante', 'Preço': 1.0},
}

cod = int(input('Digite o código do produto: '))
qtd = int(input('Digite a quantida que deseja: '))

if cod in cardapio:
    preco = cardapio[cod]['Preço']
    total = preco * qtd
    especificacao = cardapio[cod]['Especificação']
    print(f'Pedido: {qtd}x {especificacao} - Total: R${total:.2f}')
else:
    print('Código inválido!')
