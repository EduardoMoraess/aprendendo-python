#Jogo da Adivinhação v.1.0

import random

computador = random.randint(0,5)#computador pensando em um numero

print('-=' *20)
print('Vou pensando em um nuermo de 0 a 5')
print('Tente advinhar')
print('-='*20)

jogador = int(input('Digite um numero:=>'))#jogador tenta advinhar o numero

if jogador == computador:
    print('parabens voce conseguiu vencer')
else:
    print('Eu ganhei eu pensei no numero {} e voce pensou no numero {}'.format(computador, jogador))
