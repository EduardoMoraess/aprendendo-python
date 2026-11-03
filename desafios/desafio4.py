
import tkinter as tk
from tkinter import messagebox

# Preço inicial
preco = 7


# Função para calcular
def calcular_preco():
    preco = 7

    destino = destino_var.get()
    bagagem = bagagem_var.get()

    if destino == "Sim":
        preco += 3

    if bagagem == "Sim":
        preco += 2

    resultado.config(
        text=f"Preço final: R$ {preco:.2f}"
    )


# Criando janela
janela = tk.Tk()

janela.title("Calculadora de Corrida")
janela.geometry("400x450")
janela.resizable(False, False)
janela.configure(bg="#1e1e2e")


# Título
titulo = tk.Label(
    janela,
    text="Calculadora de Corrida",
    font=("Arial", 20, "bold"),
    bg="#1e1e2e",
    fg="white"
)
titulo.pack(pady=25)


# Pergunta destino
label_destino = tk.Label(
    janela,
    text="Seu destino é a UAST?",
    font=("Arial", 12),
    bg="#1e1e2e",
    fg="white"
)
label_destino.pack(pady=10)


destino_var = tk.StringVar(value="Não")

destino_menu = tk.OptionMenu(
    janela,
    destino_var,
    "Sim",
    "Não"
)
destino_menu.pack()


# Pergunta bagagem
label_bagagem = tk.Label(
    janela,
    text="Está levando bagagem pesada?",
    font=("Arial", 12),
    bg="#1e1e2e",
    fg="white"
)
label_bagagem.pack(pady=15)


bagagem_var = tk.StringVar(value="Não")

bagagem_menu = tk.OptionMenu(
    janela,
    bagagem_var,
    "Sim",
    "Não"
)
bagagem_menu.pack()


# Botão calcular
botao = tk.Button(
    janela,
    text="Calcular corrida",
    font=("Arial", 12, "bold"),
    bg="#89b4fa",
    fg="#1e1e2e",
    command=calcular_preco
)
botao.pack(pady=30)


# Resultado
resultado = tk.Label(
    janela,
    text="Preço final: R$ 7.00",
    font=("Arial", 17, "bold"),
    bg="#1e1e2e",
    fg="#a6e3a1"
)
resultado.pack(pady=10)


# Iniciar aplicação
janela.mainloop()
