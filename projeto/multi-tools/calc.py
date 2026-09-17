def media_nota():
    nota1 = float(input('Digite a primeira nota:=>'))
    nota2 = float(input('Digite a segunda nota:=>'))

    media = (nota1+nota2)/2

    if media >=7:
        print('Status: Aprovado')
    elif 5 <= media < 7:
        print('Status: Recuperação')
    else:
        print('Status: Reprovado')