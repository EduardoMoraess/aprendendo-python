#CHECADOR DE SENHAS
senha = input('digite sua senha:>')
pontos = 0

if len(senha) >= 8:
  pontos += 1
if any(c.isupper() for c in senha):
  pontos += 1
if any(c.isdigit() for c in senha):
  pontos += 1
if any(c in "!$#@" for c in senha):
  pontos += 1

#checar senha
if pontos == 4:
  print('Senha forte')
elif pontos >= 2:
  print('Senha media')
else:
  print('Senha fraca')