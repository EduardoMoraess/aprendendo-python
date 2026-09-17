def media_notas(n1, n2):
  return (n1+n2)/2

#programa principal
nota1 = float(input('Digite a primeira nota:>'))
nota2 = float(input('Digite a segunda nota:>'))

#chama a função 
media = media_notas(nota1, nota2)
print(f"\ndMedia calculada: {media:.2f}")

#verificar situação

if media >= 7:
  print("Situação: Aprovado!")
elif 5 <= media < 7:
  print('Situação: Recuperação')
else:
  print("Situação; Reprovado")