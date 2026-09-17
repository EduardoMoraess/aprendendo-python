from calc import media_nota
from porcentagem import porcentagem
from  tabuada import tabuada

import time

while True:
    print('\n===== MENU =====')
    print('1 - Média das notas')
    print('2 - Tabuada')
    print('3 - Porcentagem')
    print('0 - Sair')

    opcao = input('Digite sua escolha:=>')
    print('Analisando sua escolha')
    time.sleep(3)

    if opcao == '1':
        media_nota()
    elif opcao == '2':
        tabuada()
    elif opcao == '3':
        porcentagem()
    else:
        print('opção invalida')

    break
