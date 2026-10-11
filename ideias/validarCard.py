
def jumentinho():
    print(r"""
    ---------------------------------------------
       Bem-vindo(a), jumentinho(a) da matemática!
    ---------------------------------------------
       \    ^__^
        \   (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
    """)


def Calculadora_Inteligente():
    while True:
        jumentinho()

        print('1 - Somar')
        print('2 - Subtrair')
        print('3 - Multiplicar')
        print('4 - Dividir')
        print('0 - Sair')

        try:
            opcao = int(input('Escolha sua opção: => '))

        except ValueError:
            print('Digite uma opção válida!')
            continue

        if opcao == 0:
            print('Até logo, jumentinho!')
            break

        elif opcao in (1, 2, 3, 4):
            try:
                n1 = float(input('Digite o primeiro número: => '))
                n2 = float(input('Digite o segundo número: => '))

            except ValueError:
                print('Digite apenas números válidos!')
                continue

            if opcao == 1:
                resultado = n1 + n2
                print(f'Resultado: {resultado}')

            elif opcao == 2:
                resultado = n1 - n2
                print(f'Resultado: {resultado}')

            elif opcao == 3:
                resultado = n1 * n2
                print(f'Resultado: {resultado}')

                resposta = input(
                    'Gostaria de ver a tabuada do primeiro número? '
                ).strip().lower()

                if resposta == 'sim':
                    print(f'\nTabuada do {n1}:')

                    for i in range(1, 11):
                        print(f'{n1:g} x {i} = {n1 * i:g}')

            elif opcao == 4:
                if n2 == 0:
                    print('Não é possível dividir por zero!')
                else:
                    resultado = n1 / n2
                    print(f'Resultado: {resultado}')

        else:
            print('Opção inválida! Tente novamente.')


Calculadora_Inteligente()
