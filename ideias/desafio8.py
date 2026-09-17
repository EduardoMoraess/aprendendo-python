#sorteio de numero

import random
from time import sleep

numero_secreto = random.randint(1,100)
tentativas = 0

print('Iniciando GAME......')
sleep(3)

while True:

    palpipe = int(input('Digite seu palpite:=>'))
    tentativas +=1

    if palpipe < numero_secreto:
        print('Digite um numero maior')
    elif palpipe > numero_secreto:
        print('Digite um numero menor')
    else:
        print(f'Voce acertou o numero secreto')
        print(f'Voce precisou de {tentativas} tentativas')
        break
