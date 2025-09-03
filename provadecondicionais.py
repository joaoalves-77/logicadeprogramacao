horas_trabalhadas = float(input('Digite o total de horas trabalhadas na semana:'))
jornada_trabalhada = 44

if horas_trabalhadas > jornada_trabalhada:
    valor_hora = float(input('Digite o valor da hora normal: (R$)'))
    horas_extras = horas_trabalhadas - jornada_trabalhada
    valor_hora_extra = valor_hora * 1.5
    total_horas_extras = horas_extras * valor_hora_extra
    
    print(f'{int(horas_extras)} horas extras a R$ {valor_hora: .2f} cada.' )
    print(f'Total de horas extras: R${valor_hora_extra: .2f}')   
else:
    print('Jornada de trabalho cumprida corretamente. Não há horas extras a pagar.')