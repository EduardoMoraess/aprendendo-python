#calculadora simples

from time import sleep

numero = int(input("digite um numero:=>"))

print(f'A tabuada do numero {numero} é :')
print('Gerando tabuada.......')
sleep(3)

for contar in  range(1,11):
    print(f'{numero} x {contar} = {numero*contar}')
