def porcentagem():
  valor =  float(input('Digite um valor:=>'))
  valor_porcentagem = int(input('Digite o valor % :=>'))

  calculo = (valor * valor_porcentagem)/100

  print(f'{valor_porcentagem}% de {valor} é {calculo}')