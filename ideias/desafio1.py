print('Bem Vindo(a)')

saldo = 1200
senha = 123

while True:
  print('1 - Saldo')
  print('2 - Saque')
  print('3 - Ajuda')
  print('4 - deposito')
  print('0 - Sair')

  opcao = int(input('Digite a opção:=>'))

  if opcao == 1:
    print(f'Seu saldo é {saldo}')

  elif opcao == 2:
    print('digite sua senha')

    senha_digitada = int(input('Senha:=>'))

    if senha_digitada == senha:
      valor_saque = float(input('Digite valor que deseja sacar:=>'))

      if valor_saque <= saldo:
        saldo -= valor_saque
        print(f'valor do saque de {valor_saque:.2f} realiado com sucesso')
        print(f'Novo valor de saldo é de {saldo:.2f}')
      else:
        print('Saldo insuficiente para saque')
    else:
      print('Senha invalida! Verificar senha')

  elif opcao == 3:
    print('Entre em contato com um dos nossos gerentes')
    
  elif opcao == 4:
    print('Realizar depósito')
    valor_deposito = float(input('Valor que deseja depositar: => '))

    if valor_deposito > 0:
        saldo += valor_deposito
        print(f'Seu novo saldo é {saldo:.2f}')
    else:
        print('Digite um valor maior que zero, por favor!')
        
  elif opcao == 0:
    break
  else:
    print('opção invalida')