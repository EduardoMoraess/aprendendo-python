#criar um exemplo de caixa eletronico simples que simula as funçoes de saque e deposito!
#Usar os conhecimentos adquiridos ate agora da aula 01 ate a aula 17exercico do curso de python.

cpf_usuario = int(input('Digte seu cpf para acessar a conta:=>'))
nome_usuario = str(input('Digite seu nome:=>'))
saldo = 1200
senha = 1234

while True:
    print(f'Seja Bem-vindo(a) ao caixa {nome_usuario}')

    print('====Escolha uma opção abaixo')
    print('1 - saldo')
    print('2 - saque')
    print('3 - deposito')
    print('0 - fechar')
    opcao = int(input('escolha uma opção:=>'))

    if opcao == 1:
        print(f'Seu saldo é {saldo}')
    elif opcao == 2:
        senha_saque = int(input('Digite sua senha:=>'))
        if senha == senha_saque:
            valor_saque = float(input('Digite o valor do saque'))
            if valor_saque <= saldo:
                saldo -= valor_saque
                print(f'o valor de {valor_saque:.2f} realizado co sucesso')
                print(f'Seu novo saldo é {saldo}')
            else:
                print('Saldo insuficiente!')
        else:
            print('Senha incorreta')
    elif opcao == 3:
        senha_deposito = int(input('Digite sua senha:=>'))
        if senha_deposito == senha:
            deposito_valor = float(input('Digite o valor do desposito:=>'))

            if deposito_valor > 0:
                saldo += deposito_valor
                print(f'Seu novo saldo é {saldo:.2f}')
                print('Deposito realizado com sucesso!')
                break
            else:
                print('Digite um valor!')
        else:
            print('Senha errada, digite novamente!')
    elif opcao == 0:
        break
