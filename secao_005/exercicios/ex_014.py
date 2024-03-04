"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos pesos:
    - Trabalho de Laboratório: 2;
    - Avaliação Semestral: 3;
    - Exame Final: 5

Conforme o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
"""

notaLaboratorio = float(input('Nota de trabalho de laboratório: '))
notaAvaliacao = float(input('Nota da Avaliação Semestral: '))
notaExame = float(input('Nota Exame Final: '))
media = (notaLaboratorio * 2) + (notaAvaliacao * 3) + (notaExame * 5) / 10

if media > 0 and media <= 2.9:
    print(f'{media} - Reprovado')
elif media > 3 and media <= 4.9:
    print(f'{nota} - Recuperação')
else:
    print(f'{media} - Aprovado')
