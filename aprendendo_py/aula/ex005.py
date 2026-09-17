#Pintando Parede

altura_parede = float(input('Digite altura da parede:=>'))
largura_parede = float(input('Digite a largura da parede:=>'))

area = largura_parede * altura_parede

tinta = area /2

print(f'para pintar essa parede voce precisa de {tinta}L de tintas')