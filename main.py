def caixa_mercado():
    produto = input("nome do produto:=>")
    quantidade = int(input("quantidade de produto:=>"))
    valor = float(input("Valor do produto:=>"))

    soma = quantidade*valor

    if soma >=100:
        desconto = (soma * 10)/100
        valor_final = soma - desconto
        print(f'o valor a ser pago pelo produto {produto} é {valor_final:.2f}')
    else:
        print('Quantidade não se encaixa no desconto!')
caixa_mercado()
