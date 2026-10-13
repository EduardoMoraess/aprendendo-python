
import random

computador = random.randint(1, 100)
tentativa = 3

while tentativa > 0:
    jogador = int(input('Digite um numero entre 1 e 100: '))

    if jogador == computador:
        print('Voce acertou! Parabens!')
        break

    elif jogador < computador:
        print('O numero secreto e maior!')

    else:
        print('O numero secreto e menor!')

    tentativa -= 1

    if tentativa > 0:
        print('Voce ainda tem {} tentativa(s).'.format(tentativa))
    else:
        print('Tentativas esgotadas!')
        print('O numero secreto era {}.'.format(computador))
