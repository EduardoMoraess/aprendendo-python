import tkinter as tk
from tkinter import messagebox
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from datetime import datetime

# =====================================================
# CONFIGURAÇÕES DO BANCO
# =====================================================

SALDO_INICIAL = Decimal("1200.00")
SENHA_CORRETA = "123"

saldo = SALDO_INICIAL
historico = []

# =====================================================
# PALETA DE CORES - DARK MODERNO
# =====================================================

BG = "#0B1120"
PANEL = "#151F32"
PANEL_LIGHT = "#202D44"
PANEL_HOVER = "#293A56"

BLUE = "#477DFF"
BLUE_HOVER = "#6592FF"

CYAN = "#35D5E8"
GREEN = "#20D6A0"
GREEN_DARK = "#123D38"

RED = "#FF647C"
RED_DARK = "#402431"

WHITE = "#F4F7FC"
GRAY = "#94A3B8"
GRAY_DARK = "#64748B"

# =====================================================
# JANELA PRINCIPAL
# =====================================================

root = tk.Tk()
root.title("NEXUS BANK | Caixa Eletrônico")
root.geometry("1100x760")
root.minsize(900, 680)
root.configure(bg=BG)

root.update_idletasks()

x = (root.winfo_screenwidth() - 1100) // 2
y = (root.winfo_screenheight() - 760) // 2

root.geometry(f"1100x760+{x}+{y}")

# =====================================================
# FUNÇÕES AUXILIARES
# =====================================================

def limpar_tela():
    for widget in conteudo.winfo_children():
        widget.destroy()


def criar_texto(
    pai,
    texto,
    tamanho=12,
    cor=WHITE,
    negrito=False,
    bg=None
):
    if bg is None:
        bg = pai["bg"]

    return tk.Label(
        pai,
        text=texto,
        font=(
            "Segoe UI",
            tamanho,
            "bold" if negrito else "normal"
        ),
        bg=bg,
        fg=cor
    )


def criar_botao(
    pai,
    texto,
    comando,
    cor=BLUE,
    largura=20,
    altura=2,
    cor_texto=WHITE
):
    botao = tk.Button(
        pai,
        text=texto,
        command=comando,
        font=("Segoe UI", 11, "bold"),
        bg=cor,
        fg=cor_texto,
        activebackground=CYAN,
        activeforeground=BG,
        relief="flat",
        bd=0,
        cursor="hand2",
        width=largura,
        height=altura,
        highlightthickness=0
    )

    return botao


def formatar_moeda(valor):
    valor_formatado = f"{valor:,.2f}"
    valor_formatado = valor_formatado.replace(",", "X")
    valor_formatado = valor_formatado.replace(".", ",")
    valor_formatado = valor_formatado.replace("X", ".")

    return f"R$ {valor_formatado}"


def converter_valor(texto):
    """
    Aceita formatos como:
    100
    100.50
    100,50
    1.000,50
    """

    texto = texto.strip().replace("R$", "").replace(" ", "")

    if "," in texto:
        texto = texto.replace(".", "")
        texto = texto.replace(",", ".")

    valor = Decimal(texto)

    if not valor.is_finite():
        raise ValueError

    valor = valor.quantize(
        Decimal("0.01"),
        rounding=ROUND_HALF_UP
    )

    if valor <= 0:
        raise ValueError

    return valor


def registrar_movimentacao(tipo, valor):
    horario = datetime.now().strftime("%d/%m/%Y %H:%M")

    historico.insert(
        0,
        {
            "tipo": tipo,
            "valor": valor,
            "data": horario
        }
    )


def criar_card(pai, largura=300, altura=130, cor=PANEL):
    card = tk.Frame(
        pai,
        bg=cor,
        width=largura,
        height=altura,
        highlightbackground="#26354C",
        highlightthickness=1
    )

    card.pack_propagate(False)

    return card


# =====================================================
# CABEÇALHO
# =====================================================

header = tk.Frame(root, bg=PANEL, height=75)
header.pack(fill="x")
header.pack_propagate(False)

logo = tk.Label(
    header,
    text="◆  NEXUS BANK",
    font=("Segoe UI", 21, "bold"),
    bg=PANEL,
    fg=CYAN
)
logo.pack(side="left", padx=35)

status = tk.Label(
    header,
    text="● SISTEMA ONLINE",
    font=("Segoe UI", 9, "bold"),
    bg=PANEL,
    fg=GREEN
)
status.pack(side="right", padx=35)


# =====================================================
# ÁREA PRINCIPAL
# =====================================================

conteudo = tk.Frame(root, bg=BG)
conteudo.pack(
    fill="both",
    expand=True,
    padx=45,
    pady=20
)


# =====================================================
# TELA DE LOGIN
# =====================================================

def tela_inicial():
    limpar_tela()

    criar_texto(
        conteudo,
        "Bem-vindo ao Nexus Bank",
        28,
        WHITE,
        True
    ).pack(pady=(35, 5))

    criar_texto(
        conteudo,
        "Uma experiência bancária simples, moderna e segura.",
        11,
        GRAY
    ).pack(pady=(0, 15))

    card = criar_card(
        conteudo,
        largura=410,
        altura=490
    )
    card.pack(pady=10)

    criar_texto(
        card,
        "◈",
        48,
        CYAN,
        True
    ).pack(pady=(15, 0))

    criar_texto(
        card,
        "ACESSO À CONTA",
        16,
        WHITE,
        True
    ).pack(pady=5)

    criar_texto(
        card,
        "Digite sua senha de acesso",
        10,
        GRAY
    ).pack(pady=(0, 12))

    entrada_senha = tk.Entry(
        card,
        font=("Segoe UI", 23, "bold"),
        bg=PANEL_LIGHT,
        fg=CYAN,
        insertbackground=WHITE,
        show="●",
        justify="center",
        relief="flat",
        width=17
    )
    entrada_senha.pack(ipady=10, pady=8)

    def adicionar_numero(numero):
        if len(entrada_senha.get()) < 6:
            entrada_senha.insert(tk.END, numero)

    def apagar_numero():
        atual = entrada_senha.get()
        entrada_senha.delete(0, tk.END)
        entrada_senha.insert(0, atual[:-1])

    def verificar_senha():
        senha = entrada_senha.get()

        if senha == SENHA_CORRETA:
            tela_menu()
        else:
            messagebox.showerror(
                "Acesso negado",
                "Senha incorreta. Tente novamente."
            )

            entrada_senha.delete(0, tk.END)

    teclado = tk.Frame(card, bg=PANEL)
    teclado.pack(pady=8)

    for numero in range(1, 10):
        linha = (numero - 1) // 3
        coluna = (numero - 1) % 3

        tk.Button(
            teclado,
            text=str(numero),
            font=("Segoe UI", 12, "bold"),
            bg=PANEL_LIGHT,
            fg=WHITE,
            activebackground=BLUE,
            relief="flat",
            cursor="hand2",
            width=7,
            height=1,
            command=lambda n=numero: adicionar_numero(str(n))
        ).grid(
            row=linha,
            column=coluna,
            padx=4,
            pady=4
        )

    tk.Button(
        teclado,
        text="⌫",
        font=("Segoe UI", 12, "bold"),
        bg=RED_DARK,
        fg=RED,
        relief="flat",
        cursor="hand2",
        width=7,
        height=1,
        command=apagar_numero
    ).grid(row=3, column=0, padx=4, pady=4)

    tk.Button(
        teclado,
        text="0",
        font=("Segoe UI", 12, "bold"),
        bg=PANEL_LIGHT,
        fg=WHITE,
        relief="flat",
        cursor="hand2",
        width=7,
        height=1,
        command=lambda: adicionar_numero("0")
    ).grid(row=3, column=1, padx=4, pady=4)

    tk.Button(
        teclado,
        text="OK",
        font=("Segoe UI", 12, "bold"),
        bg=GREEN,
        fg=BG,
        relief="flat",
        cursor="hand2",
        width=7,
        height=1,
        command=verificar_senha
    ).grid(row=3, column=2, padx=4, pady=4)

    criar_botao(
        card,
        "ACESSAR CONTA  →",
        verificar_senha,
        BLUE,
        25,
        2
    ).pack(pady=12)


# =====================================================
# MENU PRINCIPAL / DASHBOARD
# =====================================================

def tela_menu():
    limpar_tela()

    topo = tk.Frame(conteudo, bg=BG)
    topo.pack(fill="x", pady=(10, 18))

    criar_texto(
        topo,
        "Visão geral",
        25,
        WHITE,
        True
    ).pack(anchor="w")

    criar_texto(
        topo,
        "Bem-vindo! O que deseja fazer hoje?",
        11,
        GRAY
    ).pack(anchor="w", pady=4)

    # Cartão do saldo

    saldo_card = tk.Frame(
        conteudo,
        bg="#172B4A",
        height=135,
        highlightbackground="#29466D",
        highlightthickness=1
    )
    saldo_card.pack(fill="x", pady=5)
    saldo_card.pack_propagate(False)

    esquerda = tk.Frame(saldo_card, bg="#172B4A")
    esquerda.pack(side="left", padx=30, pady=20)

    criar_texto(
        esquerda,
        "SALDO DISPONÍVEL",
        10,
        "#B8C9E3",
        True,
        "#172B4A"
    ).pack(anchor="w")

    criar_texto(
        esquerda,
        formatar_moeda(saldo),
        29,
        GREEN,
        True,
        "#172B4A"
    ).pack(anchor="w", pady=8)

    direita = tk.Frame(saldo_card, bg="#172B4A")
    direita.pack(side="right", padx=30)

    criar_texto(
        direita,
        "NEXUS",
        23,
        CYAN,
        True,
        "#172B4A"
    ).pack()

    criar_texto(
        direita,
        "CONTA DIGITAL",
        9,
        GRAY,
        True,
        "#172B4A"
    ).pack()

    # Operações

    criar_texto(
        conteudo,
        "Operações bancárias",
        15,
        WHITE,
        True
    ).pack(anchor="w", pady=(22, 10))

    operacoes = tk.Frame(conteudo, bg=BG)
    operacoes.pack(fill="x")

    opcoes = [
        ("▣", "CONSULTAR SALDO", "Veja seu saldo atual", tela_saldo, BLUE),
        ("＋", "FAZER DEPÓSITO", "Adicione dinheiro à conta", tela_deposito, GREEN),
        ("↗", "REALIZAR SAQUE", "Retire dinheiro da conta", tela_saque, "#A78BFA"),
        ("?", "AJUDA E SUPORTE", "Informações e atendimento", tela_ajuda, PANEL_LIGHT)
    ]

    for i, (icone, titulo, descricao, comando, cor) in enumerate(opcoes):
        linha = i // 2
        coluna = i % 2

        card = tk.Frame(
            operacoes,
            bg=PANEL,
            height=100,
            highlightbackground="#26354C",
            highlightthickness=1
        )
        card.grid(
            row=linha,
            column=coluna,
            sticky="nsew",
            padx=6,
            pady=6
        )
        card.pack_propagate(False)

        botao = tk.Button(
            card,
            text=f"{icone}   {titulo}\n      {descricao}",
            font=("Segoe UI", 11, "bold"),
            bg=PANEL,
            fg=WHITE,
            activebackground=PANEL_HOVER,
            activeforeground=WHITE,
            relief="flat",
            bd=0,
            cursor="hand2",
            anchor="w",
            justify="left",
            command=comando
        )
        botao.pack(fill="both", expand=True, padx=15, pady=10)

        botao.bind(
            "<Enter>",
            lambda event, b=botao: b.config(bg=PANEL_HOVER)
        )
        botao.bind(
            "<Leave>",
            lambda event, b=botao: b.config(bg=PANEL)
        )

    operacoes.grid_columnconfigure(0, weight=1)
    operacoes.grid_columnconfigure(1, weight=1)

    # Histórico recente

    criar_texto(
        conteudo,
        "Movimentações recentes",
        14,
        WHITE,
        True
    ).pack(anchor="w", pady=(17, 7))

    if historico:
        ultima = historico[:2]

        for item in ultima:
            cor = GREEN if item["tipo"] == "DEPÓSITO" else RED
            sinal = "+" if item["tipo"] == "DEPÓSITO" else "-"

            linha = tk.Frame(conteudo, bg=BG)
            linha.pack(fill="x", pady=2)

            criar_texto(
                linha,
                f"{item['tipo']}  •  {item['data']}",
                9,
                GRAY,
                bg=BG
            ).pack(side="left")

            criar_texto(
                linha,
                f"{sinal} {formatar_moeda(item['valor'])}",
                10,
                cor,
                True,
                BG
            ).pack(side="right")

    else:
        criar_texto(
            conteudo,
            "Nenhuma movimentação realizada até o momento.",
            10,
            GRAY
        ).pack(anchor="w")

    criar_botao(
        conteudo,
        "SAIR DA CONTA",
        tela_inicial,
        RED_DARK,
        20,
        1,
        RED
    ).pack(pady=13)


# =====================================================
# CONSULTAR SALDO
# =====================================================

def tela_saldo():
    limpar_tela()

    criar_texto(
        conteudo,
        "Seu saldo",
        26,
        WHITE,
        True
    ).pack(pady=(50, 10))

    criar_texto(
        conteudo,
        "Confira o valor disponível em sua conta.",
        11,
        GRAY
    ).pack()

    card = criar_card(
        conteudo,
        largura=520,
        altura=230
    )
    card.pack(pady=35)

    criar_texto(
        card,
        "SALDO DISPONÍVEL",
        12,
        GRAY,
        True
    ).pack(pady=(35, 10))

    criar_texto(
        card,
        formatar_moeda(saldo),
        35,
        GREEN,
        True
    ).pack(pady=10)

    criar_texto(
        card,
        "Nexus Bank • Conta digital",
        10,
        GRAY
    ).pack(pady=5)

    criar_botao(
        conteudo,
        "VOLTAR AO MENU",
        tela_menu,
        BLUE,
        25
    ).pack(pady=15)


# =====================================================
# DEPÓSITO
# =====================================================

def tela_deposito():
    limpar_tela()

    criar_texto(
        conteudo,
        "Fazer depósito",
        26,
        WHITE,
        True
    ).pack(pady=(25, 5))

    criar_texto(
        conteudo,
        "Informe quanto deseja adicionar à sua conta.",
        11,
        GRAY
    ).pack()

    card = criar_card(
        conteudo,
        largura=520,
        altura=430
    )
    card.pack(pady=20)

    criar_texto(
        card,
        "SALDO ATUAL",
        10,
        GRAY,
        True
    ).pack(pady=(20, 3))

    criar_texto(
        card,
        formatar_moeda(saldo),
        19,
        GREEN,
        True
    ).pack(pady=5)

    criar_texto(
        card,
        "VALOR DO DEPÓSITO",
        10,
        GRAY,
        True
    ).pack(pady=(15, 8))

    entrada_valor = tk.Entry(
        card,
        font=("Segoe UI", 23, "bold"),
        bg=PANEL_LIGHT,
        fg=WHITE,
        insertbackground=CYAN,
        justify="center",
        relief="flat",
        width=20
    )
    entrada_valor.pack(ipady=12, padx=35)

    entrada_valor.insert(0, "0,00")

    def selecionar_valor(valor):
        entrada_valor.delete(0, tk.END)
        entrada_valor.insert(0, str(valor))

    criar_texto(
        card,
        "VALORES RÁPIDOS",
        9,
        GRAY,
        True
    ).pack(pady=(15, 5))

    botoes = tk.Frame(card, bg=PANEL)
    botoes.pack()

    for i, valor in enumerate([50, 100, 200, 500]):
        tk.Button(
            botoes,
            text=f"R$ {valor}",
            font=("Segoe UI", 10, "bold"),
            bg=PANEL_LIGHT,
            fg=CYAN,
            activebackground=BLUE,
            relief="flat",
            cursor="hand2",
            width=9,
            height=2,
            command=lambda v=valor: selecionar_valor(v)
        ).grid(
            row=0,
            column=i,
            padx=4,
            pady=5
        )

    def confirmar_deposito():
        global saldo

        try:
            valor = converter_valor(entrada_valor.get())

        except (ValueError, InvalidOperation):
            messagebox.showerror(
                "Valor inválido",
                "Informe um valor válido para o depósito.\n\n"
                "Exemplo: 100 ou 100,50."
            )
            return

        saldo += valor

        registrar_movimentacao("DEPÓSITO", valor)

        messagebox.showinfo(
            "Depósito realizado",
            f"Depósito de {formatar_moeda(valor)} realizado!\n\n"
            f"Novo saldo: {formatar_moeda(saldo)}"
        )

        tela_menu()

    criar_botao(
        card,
        "CONFIRMAR DEPÓSITO  +",
        confirmar_deposito,
        GREEN,
        27
    ).pack(pady=15)

    criar_botao(
        conteudo,
        "VOLTAR AO MENU",
        tela_menu,
        PANEL_LIGHT,
        20
    ).pack()


# =====================================================
# REALIZAR SAQUE
# =====================================================

def tela_saque():
    limpar_tela()

    criar_texto(
        conteudo,
        "Realizar saque",
        26,
        WHITE,
        True
    ).pack(pady=(20, 5))

    criar_texto(
        conteudo,
        "Informe quanto deseja retirar da sua conta.",
        11,
        GRAY
    ).pack()

    card = criar_card(
        conteudo,
        largura=520,
        altura=430
    )
    card.pack(pady=20)

    criar_texto(
        card,
        "SALDO DISPONÍVEL",
        10,
        GRAY,
        True
    ).pack(pady=(20, 3))

    criar_texto(
        card,
        formatar_moeda(saldo),
        19,
        GREEN,
        True
    ).pack(pady=5)

    criar_texto(
        card,
        "VALOR DO SAQUE",
        10,
        GRAY,
        True
    ).pack(pady=(15, 8))

    entrada_valor = tk.Entry(
        card,
        font=("Segoe UI", 23, "bold"),
        bg=PANEL_LIGHT,
        fg=WHITE,
        insertbackground=CYAN,
        justify="center",
        relief="flat",
        width=20
    )
    entrada_valor.pack(ipady=12, padx=35)

    entrada_valor.insert(0, "0,00")

    def selecionar_valor(valor):
        entrada_valor.delete(0, tk.END)
        entrada_valor.insert(0, str(valor))

    criar_texto(
        card,
        "VALORES RÁPIDOS",
        9,
        GRAY,
        True
    ).pack(pady=(15, 5))

    botoes = tk.Frame(card, bg=PANEL)
    botoes.pack()

    for i, valor in enumerate([50, 100, 200, 500]):
        tk.Button(
            botoes,
            text=f"R$ {valor}",
            font=("Segoe UI", 10, "bold"),
            bg=PANEL_LIGHT,
            fg=CYAN,
            activebackground=BLUE,
            relief="flat",
            cursor="hand2",
            width=9,
            height=2,
            command=lambda v=valor: selecionar_valor(v)
        ).grid(
            row=0,
            column=i,
            padx=4,
            pady=5
        )

    def confirmar_saque():
        global saldo

        try:
            valor = converter_valor(entrada_valor.get())

        except (ValueError, InvalidOperation):
            messagebox.showerror(
                "Valor inválido",
                "Informe um valor válido para o saque."
            )
            return

        if valor > saldo:
            messagebox.showerror(
                "Saldo insuficiente",
                "Você não possui saldo suficiente para esse saque."
            )
            return

        saldo -= valor

        registrar_movimentacao("SAQUE", valor)

        messagebox.showinfo(
            "Saque realizado",
            f"Saque de {formatar_moeda(valor)} realizado!\n\n"
            f"Novo saldo: {formatar_moeda(saldo)}"
        )

        tela_menu()

    criar_botao(
        card,
        "CONFIRMAR SAQUE  →",
        confirmar_saque,
        BLUE,
        27
    ).pack(pady=15)

    criar_botao(
        conteudo,
        "VOLTAR AO MENU",
        tela_menu,
        PANEL_LIGHT,
        20
    ).pack()


# =====================================================
# AJUDA E SUPORTE
# =====================================================

def tela_ajuda():
    limpar_tela()

    criar_texto(
        conteudo,
        "Central de ajuda",
        26,
        WHITE,
        True
    ).pack(pady=(65, 10))

    criar_texto(
        conteudo,
        "Estamos aqui para ajudar.",
        12,
        GRAY
    ).pack()

    card = criar_card(
        conteudo,
        largura=500,
        altura=230
    )
    card.pack(pady=35)

    criar_texto(
        card,
        "◈",
        40,
        CYAN,
        True
    ).pack(pady=(20, 5))

    criar_texto(
        card,
        "PRECISA DE AJUDA?",
        17,
        WHITE,
        True
    ).pack(pady=5)

    criar_texto(
        card,
        "Este é um sistema de simulação bancária.",
        10,
        GRAY
    ).pack(pady=5)

    criar_texto(
        card,
        "Entre em contato com um gerente para obter suporte.",
        10,
        GRAY
    ).pack(pady=5)

    criar_botao(
        conteudo,
        "VOLTAR AO MENU",
        tela_menu,
        BLUE,
        25
    ).pack(pady=10)


# =====================================================
# RODAPÉ
# =====================================================

footer = tk.Label(
    root,
    text="NEXUS BANK  © 2026  |  SISTEMA DE SIMULAÇÃO BANCÁRIA",
    font=("Segoe UI", 9),
    bg=BG,
    fg=GRAY_DARK
)
footer.pack(side="bottom", pady=12)


# =====================================================
# INICIAR SISTEMA
# =====================================================

tela_inicial()

root.mainloop()
