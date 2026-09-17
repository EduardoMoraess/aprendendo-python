#sorteo da ordem de apresentação dos alunos

import random

nome1 = str(input('Digite um nome: =>'))
nome2 = str(input('Digite um nome: =>'))
nome3 = str(input('Digite um nome: =>'))
nome4 = str(input('Digite um nome: =>'))

lista = [nome1, nome2, nome3, nome4]
random.shuffle(lista)
print(f'a ordem de apresentação é {lista}')
