tempo = float(input('Digite o tempo de serviço (em anos)'))
fgts = float(input('Digite o valor do saldo Fgts: R$'))

def calcular_multa_fgts(tempo_de_serviço_anos, valor_fgts):
    if tempo_de_serviço_anos > 1:
        multa = 0.40 * valor_fgts
        return 'multa rescisória de 40%: R$ {:.2f}'.format(multa)
    else:
        return 'tempo de serviço insulficiente para multa rescisória.'
    
print(calcular_multa_fgts(tempo,fgts))

