# Analisador de Textos

from time import sleep

nome_usuario = str(input('Digte seu nome completo:=>')).strip()

print('Analisando seu nome....')
sleep(3)

print('Seu nome em maiusculas é {}'.format(nome_usuario.upper()))
print('Seu nome em minuscula é {}'.format(nome_usuario.lower()))

print('Seu nome ao todo tem {} letras'.format(len(nome_usuario)-nome_usuario.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome_usuario.find(' ')))

separa = nome_usuario.split()

#comando mais simples de se entender apesar de grande mas esta mais explicativo
print('Seu nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
