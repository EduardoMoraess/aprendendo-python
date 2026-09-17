import pyautogui
import pyperclip
import time

mensagem = input('Digite sua mensagem aqui:=>')
quantidade = int(input('Quantidade de mensagens:=>'))

print('Voce tem 10 segundos para clicar no campo de enviar a mensagem')
time.sleep(10)

pyperclip.copy(mensagem)

for i in range(quantidade):
    pyautogui.hotkey('ctrl', 'v')
    pyautogui.press('enter')
    time.sleep(0.5)

print('envio concluido')
