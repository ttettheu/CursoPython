"""
Faça um programa que leia o horário (hora, minuto e segundo) de início e a duração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do término da mesma.
"""

print('Digite o horário de início da experiência abaixo:')

hora = int(input('Hora: '))
minuto = int(input('Minuto: '))
segundo = int(input('Segundo: '))
duracao = int(input('Duração da experiência (segundos): '))

segundoFinal = (segundo + duracao) % 60
minutoFinal = (minuto + (segundo + duracao) // 60) % 60
horaFinal = (hora + (minuto + (segundo + duracao) // 60) // 60) % 24

print(f'Fim do evento: {horaFinal}h {minutoFinal}min e {segundoFinal} segundos')
