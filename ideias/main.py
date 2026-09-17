def media_notas(n1, n2):
  return (n1+n2)/2

nota1 = float(input('Digite sua primeira nota:>'))
nota2 = float(input('Digite sua segunda nota:>'))

media = media_notas(nota1, nota2)
print(f'\n Media: {media:.2f}')

#checar notas
if media >= 7:
  print('Situação: Aprovado')
elif 5 <= media < 7:
  print('Situação: Recuperação')
else:
  print('Situação: Reprovado')