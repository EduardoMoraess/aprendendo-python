import random

numero_secreto = random.randint(1, 100)
tentativas = 0

print('iniciando jogo')

while True:
  palpites = int(input('Digite seu palpite'))
  tentativas += 1

  if palpites > numero_secreto:
    print('Digite um numero Menor')
  elif palpites < numero_secreto:
    print('Digite um numero Maior')
  else:
    print('Parabens voce acertou')
    print(f'Foram necessario {tentativas} tentativas')

    break