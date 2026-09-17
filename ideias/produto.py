# calculando valor de um produto

valor_produto = float(input('Digite o valor do produto: R$ '))

while True:
    print('\n=============== Menu ============')
    print('1 - À vista (5% de desconto)')
    print('2 - Parcelado (10% de acréscimo)')
    print('3 - Débito (Valor normal)')
    print('4 - Sair')

    opcao = int(input('Digite a opção de pagamento:=> '))

    if opcao == 1:
        preco_final = valor_produto * 0.95
        print(f'\nO seu produto à vista custa: R$ {preco_final:.2f}')
        break  # Encerra o loop após concluir o pagamento
    elif opcao == 2:
        preco_final = valor_produto * 1.10
        print(f'\nO produto parcelado custa: R$ {preco_final:.2f}')
        break  # Encerra o loop após concluir o pagamento
    elif opcao == 3:
        preco_final = valor_produto
        print(f'\nO produto no débito custa: R$ {preco_final:.2f}')
        break  # Encerra o loop após concluir o pagamento
    elif opcao == 4:
        print('\nOperação cancelada.')
        break
    else:
        print('\nOpção inválida! Tente novamente.')