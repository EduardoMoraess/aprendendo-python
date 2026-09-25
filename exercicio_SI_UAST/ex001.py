idade_user = int(input("digite sua idade:=>"))

if idade_user >= 18:
    print("Voce ja pode voltar")
elif idade_user <=17 or idade_user >70:
    print("Voto opcional!")
else:
    print("Digite uma idade valida!")
