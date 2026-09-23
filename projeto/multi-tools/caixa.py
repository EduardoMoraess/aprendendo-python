print('Bem-vindo(a)')

saldo = 1200
senha = 123

while True:

    print('======= Menu =======\n')
    print('1 - Saldo')
    print('2 - Saque')
    print('3 - Ajuda')
    print('0 - Sair')

    opcao = int(input('Digite uma Opção: => '))

    if opcao == 1:
        print(f'Seu saldo é R$ {saldo:.2f}')

    elif opcao == 2:

        senha_digitada = int(input('Digite sua senha: => '))

        if senha_digitada == senha:

            valor_saque = float(input('Digite o valor que deseja sacar: => '))

            if valor_saque <= saldo:

                saldo -= valor_saque

                print(f'Saque no valor de R$ {valor_saque:.2f} realizado com sucesso!')
                print(f'Seu novo saldo é R$ {saldo:.2f}')

            else:

                print('Saldo insuficiente!')

        else:

            print('Senha inválida!')

    elif opcao == 3:

        print('Procure um de nossos gerentes!')

    elif opcao == 0:

        print('Obrigado por utilizar nosso banco!')
        break

    else:

        print('Opção inválida!')
