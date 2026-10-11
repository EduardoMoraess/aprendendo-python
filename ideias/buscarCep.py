
import re
import requests


def exibir_cabecalho():
    print("\033[96m")
    print("╭──────────────────────────────────────────╮")
    print("│          CONSULTA DE CEPs                │")
    print("│          Busca de endereços              │")
    print("╰──────────────────────────────────────────╯")
    print("\033[0m")


def consultar_cep(cep):
    cep = re.sub(r"\D", "", cep)

    if len(cep) != 8:
        print("\n[ERRO] Digite um CEP com 8 números.")
        return

    url = f"https://viacep.com.br/ws/{cep}/json/"

    try:
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        dados = resposta.json()

        if dados.get("erro"):
            print(f"\n[ERRO] CEP {cep} não encontrado.")
            return

        print("\n\033[92m╭────────── ENDEREÇO ENCONTRADO ──────────╮")
        print(f"│ CEP:       {dados.get('cep', 'N/A')}")
        print(f"│ Rua:       {dados.get('logradouro') or 'Não informado'}")
        print(f"│ Bairro:    {dados.get('bairro') or 'Não informado'}")
        print(f"│ Cidade:    {dados.get('localidade') or 'Não informado'}")
        print(f"│ Estado:    {dados.get('uf') or 'Não informado'}")
        print("╰─────────────────────────────────────────╯\033[0m")

    except requests.RequestException:
        print("\n[ERRO] Não foi possível conectar à API.")
        print("Verifique sua conexão com a internet.")


def consultar_varios():
    print("\nDigite os CEPs separados por vírgula.")
    entrada = input("CEPs: ").strip()

    ceps = entrada.split(",")

    for cep in ceps:
        print("\n" + "─" * 44)
        consultar_cep(cep.strip())


def menu():
    while True:
        exibir_cabecalho()

        print("  [1] Consultar um CEP")
        print("  [2] Consultar vários CEPs")
        print("  [0] Sair")

        opcao = input("\n  Escolha uma opção: ").strip()

        if opcao == "1":
            cep = input("\n  Digite o CEP: ")
            consultar_cep(cep)

        elif opcao == "2":
            consultar_varios()

        elif opcao == "0":
            print("\nAté mais! Obrigado por utilizar.")
            break

        else:
            print("\n[ERRO] Opção inválida.")

        input("\nPressione ENTER para continuar...")


if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        print("\n\nPrograma encerrado.")
