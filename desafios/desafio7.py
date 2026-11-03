#joguinho de advinha numero

import random

#validar o numero do jodor
while True:
    #computador
    computador = random.randint(1,100)
    #jogador
    jogador = int(input('Digite um numero:=>'))

    if jogador == computador:
        print('Voce acertou')
    elif jogador > computador:
        print('digite um numero menor')
    elif jogador < computador:
        print('digite um numero maior')
    else:
        print('digite apenas numeros')
