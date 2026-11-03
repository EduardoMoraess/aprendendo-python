def media_aluno(n1, n2):
    return (n1 + n2)/2

nota1 =  float(input('digite sua nota:=>'))
nota2 =  float(input('digite sua nota:=>'))

media = media_aluno(nota1, nota2)

if media >= 7:
    print(f'Aprovado com media {media:.2f}')
else:
    print(f"Reprovado sua media foi {media:.2f}")
