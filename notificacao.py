import tkinter as tk
from tkinter import messagebox
import subprocess

def mostrar_aviso():
    titulo = entrada_titulo.get().strip()
    mensagem = entrada_mensagem.get().strip()
    motivo = entrada_motivo.get().strip()
    tempo = entrada_tempo.get().strip()

    if not titulo or not mensagem or not motivo or not tempo:
        messagebox.showwarning(
            "Campos vazios",
            "Preencha todos os campos!"
        )
        return

    try:
        tempo = int(tempo)

        if tempo < 0:
            raise ValueError

    except ValueError:
        messagebox.showerror(
            "Erro",
            "Digite um tempo válido em segundos."
        )
        return

    janela.withdraw()

    def enviar_notificacao():
        texto = f"{mensagem}\nMotivo: {motivo}"

        try:
            subprocess.run(
                ["notify-send", titulo, texto],
                check=True
            )
        except FileNotFoundError:
            messagebox.showerror(
                "Erro",
                "O comando notify-send não está instalado."
            )
        except subprocess.CalledProcessError:
            messagebox.showerror(
                "Erro",
                "Não foi possível mostrar a notificação."
            )
        finally:
            janela.deiconify()

    janela.after(tempo * 1000, enviar_notificacao)


def visualizar_aviso():
    titulo = entrada_titulo.get().strip() or "Aviso"
    mensagem = entrada_mensagem.get().strip()
    motivo = entrada_motivo.get().strip()

    if not mensagem:
        mensagem = "Esta é uma notificação de teste."

    if motivo:
        mensagem += f"\nMotivo: {motivo}"

    messagebox.showinfo(titulo, mensagem)


janela = tk.Tk()
janela.title("Gerenciador de avisos")
janela.geometry("420x390")
janela.resizable(False, False)

tk.Label(
    janela,
    text="Criar notificação",
    font=("Arial", 17, "bold")
).pack(pady=15)

tk.Label(janela, text="Título do aviso:").pack()
entrada_titulo = tk.Entry(janela, width=45)
entrada_titulo.insert(0, "Aviso")
entrada_titulo.pack(pady=4)

tk.Label(janela, text="Mensagem:").pack()
entrada_mensagem = tk.Entry(janela, width=45)
entrada_mensagem.insert(0, "Hora de estudar Python")
entrada_mensagem.pack(pady=4)

tk.Label(janela, text="Motivo do aviso:").pack()
entrada_motivo = tk.Entry(janela, width=45)
entrada_motivo.insert(0, "Não esquecer os estudos")
entrada_motivo.pack(pady=4)

tk.Label(
    janela,
    text="Aparecer depois de quantos segundos?"
).pack(pady=(8, 0))

entrada_tempo = tk.Entry(janela, width=15)
entrada_tempo.insert(0, "10")
entrada_tempo.pack(pady=4)

tk.Button(
    janela,
    text="Agendar aviso",
    command=mostrar_aviso,
    bg="#2196F3",
    fg="white",
    width=22
).pack(pady=8)

tk.Button(
    janela,
    text="Visualizar teste",
    command=visualizar_aviso,
    width=22
).pack()

janela.mainloop()
