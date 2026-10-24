
import pyautogui
import pyperclip
import time

mensagem = input("Digite sua mensagem: ")
quantidade = int(input("Quantidade de mensagens: "))

if quantidade <= 0:
    print("Digite uma quantidade maior que zero.")
    raise SystemExit

print("Você tem 10 segundos para selecionar o campo de texto.")
time.sleep(10)

pyperclip.copy(mensagem)

for i in range(quantidade):
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(0.5)

print("Envio concluído!")
