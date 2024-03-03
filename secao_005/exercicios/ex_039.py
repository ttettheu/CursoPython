"""
Uma empresa decide dar um aumento aos seus funcionários de acordo com uma tabela
que considera o salário atual e o tempo de serviço de cada funcionário. Os funionários
com menor salário terão um aumento proporcionalmente maior do que os funionários
com um saláriio maior, e conforme o tempo de serviço na empresa, cada funcionário irá
receber um bônus adicional de salário. Faça um programa que leia:
    - O valor do salário atual do funcionário;
    - O tempo de serviço desse funcionário na empresa (número de anos de trabalho na empresa).

Use as tabelas abaixo para calcular o salário reajustado deste funcionário e imprima o
valor do salário final reajustado, ou uma mensagem caso o funcionário não tenha direito
a nenhum aumento.

    |  SALÁRIO ATUAL   | REAJUSTE (%) | TEMPO DE SERVIÇO |   BÔNUS   |
    | Até 500,00       |      25%     | Abaixo de 1 anos | Sem bônus |
    | Até 1000,00      |      20%     |   De 1 a 3 anos  |   100,00  |
    | Até 1500,00      |      15%     |   De 4 a 6 anos  |   200,00  |
    | Até 2000,00      |      10%     |  De 7 a 10 anos  |   300,00  |
    | Acima de 2000,00 | Sem reajuste |  Mais de 10 anos |   500,00  |

"""
