#preço da corrida
preco = 7.00

#coletar  as informações e padronizar
destino = input("Passageiro vai pra UAST sim/não:=>").lower()
bagagem = input("esta levando bagagem pesada sim/não:=>").lower()

#condição para calcular a taxa da viagem
if destino == 'sim':
    print("Seu destino é muito longe tera uma taxa")
    preco += 3
else:
    print(f'Preço normal de {preco}')

#taxa com bagagem
if bagagem == 'sim':
    print('vai aumentar mais 2 reais na corrida')
    preco += 2
else:
    print(f'Preço normal de {preco}')

print(f'Valor final da corrida vai ser {preco:.2f}')
