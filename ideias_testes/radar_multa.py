# radar de multas

from time import sleep

lista_km = [
    'De 50km a 80km esta dentro do limite',
    'De 81km a 90km esta acima do limite',
    'Mais que o permitido: multa gravissima por risco de acidente'
]

velocidade_km = int(input('Digite sua velocidade KM/H:=> '))

print('Analisando sua velocidade')
sleep(3)

if velocidade_km <= 50 and velocidade_km <= 80:

    print(lista_km[0])

elif velocidade_km >= 81 and velocidade_km <= 90:

    print(lista_km[1])

else:

    print(lista_km[2])
