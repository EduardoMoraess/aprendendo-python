#jogo de advinhar um numero

import random

computador = random.randint(1, 100)#computador pensar

jogador = int(input('Digite um numero entre 1 e 100:=>'))

if jogador == computador:
    print('Voce acertou')
elif jogador < computador:
    print('Numero é maior que {}'.format(jogador))
elif jogador > computador:
    print('Numero menor que {}'.format(jogador))
else:
    print('Computador venceu!')
