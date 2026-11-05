#tabuada inteligente
#Tabuada inteligente
#Peça um número.Mostre a tabuada de 1 até 10.Pergunte se deseja calcular outra tabuada.#

from time import sleep
print('+='*30)
print('Bem-vindo a tabuada jeguinho(a)')
print('+='*30)

while True:
    print('1 gerar tabuada')
    print('2 sair')

    opcao = int(input('Digite sua opção:=>'))

    if opcao == 1:
        numero = int(input('digite um numero:=>'))
        print('Gerando a tabuada....')
        sleep(3)

        print(f'A tabuada do numero {numero} é:')

        for count in range(1,11):
            print(f'{numero} x {count} = {numero*count}')
    else:
        print('fechando a tabuada....')
        break
