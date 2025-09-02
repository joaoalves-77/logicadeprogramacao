notas_e_moedas = [200, 100, 50, 20, 10, 5, 2, 1, 0.50, 0.25, 0.10, 0.05, 0.01]

valor_a_receber = float(input("Digite o valor a receber?: "))

valor_recebido = float(input("Digite o valor recebido?: "))


diferenca = valor_recebido - valor_a_receber

for valor in notas_e_moedas:
    quantidade_de_itens = 0
    
    while valor <= diferença: 
        quantidade_de_itens += 1
        diferença -= valor
        if quantidade_de_itens > 0:
          print(f'{quantidade_de_itens} itens de {valor} ')
            