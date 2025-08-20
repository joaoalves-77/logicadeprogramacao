#contador = 0
numero1 = int(input(input("digite um inteiro")))
numero2 = int(input('digite outro inteiro'))

while numero1 != numero2 :

   if numero1 > numero2:
      diferenca = numero1 - numero2
      numero1 = diferenca

   else: 
      diferenca = numero2 - numero1
      numero2 = diferenca

print('numero iguais')
