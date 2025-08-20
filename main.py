import random

numero_aleatorio = random.randint(1,10)
palpite_jogador = int(input('digite um numeiro inteiro de 1 a 10'))
numero_tentativas = 1

while numero_aleatorio != palpite_jogador:
    numero_tentativas += 1

    if palpite_jogador > numero_aleatorio:
        print('muito alto')
    else:
        print('muito baixo')

    palpite_jogador = int(input('digite um inteiro de 1 a 10'))
    
print(f"acertou em {numero_tentativas} tentativas")
