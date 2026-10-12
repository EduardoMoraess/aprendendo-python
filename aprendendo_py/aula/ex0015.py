#Par ou Ímpar?

numero = int(input('Digite um numero:=>'))

if numero %2 == 0:
    print('\033[32mPar\033[0m')
else:
    print("\033[31mImpar\033[0m")
