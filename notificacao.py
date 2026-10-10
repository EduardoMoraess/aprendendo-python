
from __future__ import annotations

import shutil
import subprocess
import tkinter as tk
from tkinter import messagebox, ttk


class GerenciadorAvisos:
    """Aplicação para criar, visualizar e agendar notificações no Linux."""

    # Paleta de cores
    BG = "#11131C"
    SURFACE = "#191C28"
    INPUT_BG = "#222636"
    PRIMARY = "#8B7CFF"
    PRIMARY_HOVER = "#A196FF"
    TEXT = "#F0F1FA"
    MUTED = "#9298B0"
    SUCCESS = "#63D6A5"
    DANGER = "#FF7185"
    BORDER = "#303449"

    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Avisos Pro")
        self.root.geometry("520x650")
        self.root.minsize(480, 610)
        self.root.configure(bg=self.BG)

        self.after_id: str | None = None
        self.tempo_restante = 0

        self.titulo_var = tk.StringVar(value="Aviso")
        self.mensagem_var = tk.StringVar(
            value="Hora de estudar Python"
        )
        self.motivo_var = tk.StringVar(
            value="Não esquecer os estudos"
        )
        self.tempo_var = tk.StringVar(value="10")
        self.status_var = tk.StringVar(
            value="Pronto para criar uma notificação."
        )

        self._configurar_estilos()
        self._construir_interface()
        self._atualizar_botoes()

        self.root.protocol("WM_DELETE_WINDOW", self._ao_fechar)

    # --------------------------------------------------
    # CONFIGURAÇÃO VISUAL
    # --------------------------------------------------

    def _configurar_estilos(self) -> None:
        style = ttk.Style()

        style.theme_use("clam")

        style.configure(
            "App.TFrame",
            background=self.BG,
        )

        style.configure(
            "Card.TFrame",
            background=self.SURFACE,
        )

        style.configure(
            "App.TLabel",
            background=self.BG,
            foreground=self.TEXT,
            font=("DejaVu Sans", 10),
        )

        style.configure(
            "Title.TLabel",
            background=self.BG,
            foreground=self.TEXT,
            font=("DejaVu Sans", 23, "bold"),
        )

        style.configure(
            "Subtitle.TLabel",
            background=self.BG,
            foreground=self.MUTED,
            font=("DejaVu Sans", 10),
        )

        style.configure(
            "Section.TLabel",
            background=self.SURFACE,
            foreground=self.TEXT,
            font=("DejaVu Sans", 11, "bold"),
        )

        style.configure(
            "Field.TLabel",
            background=self.SURFACE,
            foreground=self.MUTED,
            font=("DejaVu Sans", 9),
        )

        style.configure(
            "Status.TLabel",
            background=self.SURFACE,
            foreground=self.MUTED,
            font=("DejaVu Sans", 9),
        )

        style.configure(
            "App.TEntry",
            fieldbackground=self.INPUT_BG,
            foreground=self.TEXT,
            insertcolor=self.TEXT,
            bordercolor=self.BORDER,
            lightcolor=self.BORDER,
            darkcolor=self.BORDER,
            padding=10,
            relief="flat",
        )

        style.configure(
            "Primary.TButton",
            background=self.PRIMARY,
            foreground="#FFFFFF",
            font=("DejaVu Sans", 10, "bold"),
            padding=(14, 11),
            borderwidth=0,
        )

        style.map(
            "Primary.TButton",
            background=[
                ("disabled", "#45415F"),
                ("active", self.PRIMARY_HOVER),
            ],
            foreground=[
                ("disabled", "#A4A0B9"),
            ],
        )

        style.configure(
            "Secondary.TButton",
            background=self.INPUT_BG,
            foreground=self.TEXT,
            font=("DejaVu Sans", 9, "bold"),
            padding=(12, 10),
            borderwidth=0,
        )

        style.map(
            "Secondary.TButton",
            background=[
                ("disabled", self.SURFACE),
                ("active", self.BORDER),
            ],
        )

        style.configure(
            "Cancel.TButton",
            background="#39232D",
            foreground=self.DANGER,
            font=("DejaVu Sans", 9, "bold"),
            padding=(12, 10),
            borderwidth=0,
        )

        style.map(
            "Cancel.TButton",
            background=[("active", "#51303D")],
        )

    def _construir_interface(self) -> None:
        container = ttk.Frame(
            self.root,
            style="App.TFrame",
            padding=(28, 24, 28, 20),
        )
        container.pack(fill="both", expand=True)

        # Cabeçalho
        ttk.Label(
            container,
            text="AVISOS / LINUX",
            foreground=self.PRIMARY,
            background=self.BG,
            font=("DejaVu Sans", 9, "bold"),
        ).pack(anchor="w")

        ttk.Label(
            container,
            text="Avisos Pro",
            style="Title.TLabel",
        ).pack(anchor="w", pady=(5, 2))

        ttk.Label(
            container,
            text="Crie lembretes e organize seu tempo.",
            style="Subtitle.TLabel",
        ).pack(anchor="w", pady=(0, 20))

        # Cartão principal
        card = ttk.Frame(
            container,
            style="Card.TFrame",
            padding=20,
        )
        card.pack(fill="both", expand=True)

        ttk.Label(
            card,
            text="Nova notificação",
            style="Section.TLabel",
        ).pack(anchor="w", pady=(0, 17))

        self._criar_campo(
            card, "TÍTULO DO AVISO", self.titulo_var
        )

        self._criar_campo(
            card, "MENSAGEM", self.mensagem_var
        )

        self._criar_campo(
            card, "MOTIVO DO AVISO", self.motivo_var
        )

        ttk.Label(
            card,
            text="ATRASO PARA EXIBIÇÃO (SEGUNDOS)",
            style="Field.TLabel",
        ).pack(anchor="w", pady=(4, 7))

        self.tempo_entry = ttk.Entry(
            card,
            textvariable=self.tempo_var,
            style="App.TEntry",
            width=15,
        )
        self.tempo_entry.pack(anchor="w", fill="x")

        # Botões
        botoes = ttk.Frame(
            card,
            style="Card.TFrame",
        )
        botoes.pack(fill="x", pady=(22, 0))

        ttk.Button(
            botoes,
            text="Agendar aviso",
            style="Primary.TButton",
            command=self.agendar_aviso,
        ).pack(fill="x", pady=(0, 9))

        linha_botoes = ttk.Frame(
            botoes,
            style="Card.TFrame",
        )
        linha_botoes.pack(fill="x")

        ttk.Button(
            linha_botoes,
            text="Visualizar teste",
            style="Secondary.TButton",
            command=self.visualizar_aviso,
        ).pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 5),
        )

        self.cancelar_btn = ttk.Button(
            linha_botoes,
            text="Cancelar aviso",
            style="Cancel.TButton",
            command=self.cancelar_aviso,
        )
        self.cancelar_btn.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(5, 0),
        )

        # Rodapé e estado da aplicação
        rodape = ttk.Frame(
            container,
            style="App.TFrame",
        )
        rodape.pack(fill="x", pady=(15, 0))

        ttk.Label(
            rodape,
            text="●",
            foreground=self.SUCCESS,
            background=self.BG,
            font=("DejaVu Sans", 11),
        ).pack(side="left", padx=(0, 7))

        ttk.Label(
            rodape,
            textvariable=self.status_var,
            style="Subtitle.TLabel",
        ).pack(side="left", fill="x", expand=True)

        ttk.Label(
            container,
            text="Desenvolvido em Python • Tkinter",
            foreground=self.MUTED,
            background=self.BG,
            font=("DejaVu Sans", 8),
        ).pack(pady=(12, 0))

    def _criar_campo(
        self,
        parent: ttk.Frame,
        rotulo: str,
        variavel: tk.StringVar,
    ) -> None:
        ttk.Label(
            parent,
            text=rotulo,
            style="Field.TLabel",
        ).pack(anchor="w", pady=(0, 7))

        ttk.Entry(
            parent,
            textvariable=variavel,
            style="App.TEntry",
        ).pack(fill="x", pady=(0, 15))

    # --------------------------------------------------
    # VALIDAÇÃO
    # --------------------------------------------------

    def _obter_dados(self) -> dict[str, str | int] | None:
        titulo = self.titulo_var.get().strip()
        mensagem = self.mensagem_var.get().strip()
        motivo = self.motivo_var.get().strip()
        tempo_texto = self.tempo_var.get().strip()

        if not all((titulo, mensagem, motivo, tempo_texto)):
            messagebox.showwarning(
                "Campos obrigatórios",
                "Preencha todos os campos antes de continuar.",
                parent=self.root,
            )
            return None

        try:
            tempo = int(tempo_texto)

            if tempo < 0:
                raise ValueError

        except ValueError:
            messagebox.showerror(
                "Tempo inválido",
                "Digite um número inteiro igual ou superior a zero.",
                parent=self.root,
            )
            return None

        return {
            "titulo": titulo,
            "mensagem": mensagem,
            "motivo": motivo,
            "tempo": tempo,
        }

    # --------------------------------------------------
    # NOTIFICAÇÕES
    # --------------------------------------------------

    def _enviar_notificacao(
        self,
        titulo: str,
        mensagem: str,
        motivo: str,
    ) -> bool:
        comando = shutil.which("notify-send")

        if comando is None:
            messagebox.showerror(
                "Dependência ausente",
                "O comando notify-send não foi encontrado.\n\n"
                "Em distribuições Debian/Ubuntu, instale-o com:\n"
                "sudo apt install libnotify-bin",
                parent=self.root,
            )
            return False

        texto = f"{mensagem}\nMotivo: {motivo}"

        try:
            subprocess.run(
                [comando, titulo, texto],
                check=True,
                timeout=10,
                capture_output=True,
                text=True,
            )

            return True

        except subprocess.TimeoutExpired:
            messagebox.showerror(
                "Tempo excedido",
                "O sistema demorou demais para processar a notificação.",
                parent=self.root,
            )

        except subprocess.CalledProcessError:
            messagebox.showerror(
                "Falha na notificação",
                "O sistema não conseguiu exibir a notificação.",
                parent=self.root,
            )

        except OSError as erro:
            messagebox.showerror(
                "Erro do sistema",
                f"Não foi possível executar o comando.\n{erro}",
                parent=self.root,
            )

        return False

    def agendar_aviso(self) -> None:
        dados = self._obter_dados()

        if dados is None:
            return

        if self.after_id is not None:
            messagebox.showwarning(
                "Aviso já agendado",
                "Cancele o aviso atual antes de agendar outro.",
                parent=self.root,
            )
            return

        titulo = str(dados["titulo"])
        mensagem = str(dados["mensagem"])
        motivo = str(dados["motivo"])
        tempo = int(dados["tempo"])

        self.tempo_restante = tempo

        self.after_id = self.root.after(
            tempo * 1000,
            lambda: self._executar_agendamento(
                titulo,
                mensagem,
                motivo,
            ),
        )

        self.status_var.set(
            f"Aviso agendado para daqui a {tempo} segundo(s)."
        )
        self._atualizar_botoes()

    def _executar_agendamento(
        self,
        titulo: str,
        mensagem: str,
        motivo: str,
    ) -> None:
        self.after_id = None

        sucesso = self._enviar_notificacao(
            titulo,
            mensagem,
            motivo,
        )

        if sucesso:
            self.status_var.set("Notificação enviada com sucesso.")
        else:
            self.status_var.set("Não foi possível enviar a notificação.")

        self._atualizar_botoes()

    def visualizar_aviso(self) -> None:
        titulo = self.titulo_var.get().strip() or "Aviso"
        mensagem = (
            self.mensagem_var.get().strip()
            or "Esta é uma notificação de teste."
        )
        motivo = self.motivo_var.get().strip()

        if motivo:
            mensagem += f"\n\nMotivo: {motivo}"

        messagebox.showinfo(
            titulo,
            mensagem,
            parent=self.root,
        )

    def cancelar_aviso(self) -> None:
        if self.after_id is None:
            return

        self.root.after_cancel(self.after_id)
        self.after_id = None
        self.tempo_restante = 0

        self.status_var.set("Agendamento cancelado.")
        self._atualizar_botoes()

    def _atualizar_botoes(self) -> None:
        estado = "normal" if self.after_id is not None else "disabled"
        self.cancelar_btn.configure(state=estado)

    def _ao_fechar(self) -> None:
        if self.after_id is not None:
            self.root.after_cancel(self.after_id)
            self.after_id = None

        self.root.destroy()


def main() -> None:
    root = tk.Tk()
    GerenciadorAvisos(root)
    root.mainloop()


if __name__ == "__main__":
    main()
