
usuarios = {}

while True:
    print('\n=== MENU ===')
    print('1 - Cadastrar usuario')
    print('2 - Fazer login')
    print('3 - Listar usuarios')
    print('4 - Sair')

    opcao = input('Escolha: ')

    if opcao == '1':
        nome = input('Novo usuario: ')
        senha = input('Nova senha: ')

        usuarios[nome] = senha
        print('Usuario cadastrado!')

    elif opcao == '2':
        login = input('Usuario: ')
        senha = input('Senha: ')

        if login in usuarios and usuarios[login] == senha:
            print('Login realizado com sucesso!')
        else:
            print('Dados incorretos!')

    elif opcao == '3':
        print(usuarios)

    elif opcao == '4':
        print('Saindo...')
        break

    else:
        print('Opcao invalida!')
