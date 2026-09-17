import random
import time

numero_secreto = random.randint(1, 100)
tentativas = 0

print('INICIANOO O GAME....')

time.sleep(5)

print('GAME INICIADO')

while True:
  
  palpite = int(input('Digite seu palpite:>'))
  tentativas +=1

  if palpite < numero_secreto:
    print('tente um numero MAIOR!')
  elif palpite > numero_secreto:
    print('tente um numero MENOR')
  else:
    print('Parabens! Voce acertou')
    print(f'Voce precisou de {tentativas} tentivas')

    break
