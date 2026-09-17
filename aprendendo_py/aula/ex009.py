#sorteador de nome de alunos

import random

nome1 = str(input('Digite um nome:=>'))
nome2 = str(input('Digite um nome:=>'))
nome3 = str(input('Digite um nome:=>'))
nome4 = str(input('Digite um nome:=>'))

lista = [nome1, nome2, nome3, nome4]

escolhido = random.choice(lista)

print(f'o escolhido foi {escolhido}')
