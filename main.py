reservatorio = {
    "capacidade": 10000.0,
    "nivel": 7500.0
}


def mostrar_status():
    capacidade = reservatorio["capacidade"]
    nivel = reservatorio["nivel"]

    porcentagem = (nivel / capacidade) * 100

    print("\n===== STATUS DO RESERVATÓRIO =====")
    print(f"Capacidade: {capacidade:.1f} litros")
    print(f"Nível atual: {nivel:.1f} litros")
    print(f"Percentual: {porcentagem:.1f}%")

    if porcentagem <= 20:
        print("⚠️ ALERTA: nível crítico!")

    elif porcentagem <= 40:
        print("⚠️ Atenção: nível baixo.")

    else:
        print("✅ Nível normal.")


def abastecer():
    quantidade = float(input("Quantidade de água para abastecer: "))

    capacidade = reservatorio["capacidade"]
    nivel = reservatorio["nivel"]

    if quantidade <= 0:
        print("❌ Quantidade inválida.")

    elif nivel + quantidade > capacidade:
        print("❌ O reservatório não possui espaço suficiente.")

    else:
        reservatorio["nivel"] += quantidade
        print("✅ Reservatório abastecido.")


def consumir():
    quantidade = float(input("Quantidade consumida: "))

    nivel = reservatorio["nivel"]

    if quantidade <= 0:
        print("❌ Quantidade inválida.")

    elif quantidade > nivel:
        print("❌ Água insuficiente no reservatório.")

    else:
        reservatorio["nivel"] -= quantidade
        print("✅ Consumo registrado.")


while True:

    print("\n===== SISTEMA DE ABASTECIMENTO =====")
    print("1 - Ver reservatório")
    print("2 - Abastecer")
    print("3 - Registrar consumo")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_status()

    elif opcao == "2":
        abastecer()

    elif opcao == "3":
        consumir()

    elif opcao == "4":
        print("Sistema encerrado.")
        break

    else:
        print("❌ Opção inválida.")
