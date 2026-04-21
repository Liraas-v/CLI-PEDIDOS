import csv

ARQUIVO = "pedidos.csv"


# -------------------------------
# Validação
# -------------------------------
def validar_valor(valor):
    try:
        float(valor)
        return True
    except:
        return False


# -------------------------------
# Adicionar pedido
# -------------------------------
def adicionar_pedido():
    cliente = input("Nome do cliente: ")
    servico = input("Serviço: ")

    while True:
        valor = input("Valor: ")
        if validar_valor(valor):
            break
        else:
            print("❌ Valor inválido! Digite apenas números.")

    with open(ARQUIVO, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([cliente, servico, valor, "Em andamento"])

    print("Pedido adicionado com sucesso!")


# -------------------------------
# Listar pedidos
# -------------------------------
def listar_pedidos():
    with open(ARQUIVO, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)  # pula cabeçalho

        print("\nPEDIDOS:\n")
        for i, linha in enumerate(reader, start=1):
            print(f"{i}. Cliente: {linha[0]}")
            print(f"   Serviço: {linha[1]}")
            print(f"   Valor: R${linha[2]}")
            print(f"   Status: {linha[3]}")
            print("-" * 30)


# -------------------------------
# Atualizar status
# -------------------------------
def atualizar_status():
    pedidos = []

    with open(ARQUIVO, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        cabecalho = next(reader)
        pedidos = list(reader)

    if not pedidos:
        print("Nenhum pedido encontrado.")
        return

    listar_pedidos()

    try:
        indice = int(input("Número do pedido: ")) - 1

        if indice < 0 or indice >= len(pedidos):
            print("❌ Pedido inválido.")
            return

        novo_status = input("Novo status: ")
        pedidos[indice][3] = novo_status

        with open(ARQUIVO, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(cabecalho)
            writer.writerows(pedidos)

        print("Status atualizado!")

    except ValueError:
        print("Digite um número válido.")


# -------------------------------
# Menu principal
# -------------------------------
def menu():
    while True:
        print("\n--- SISTEMA LAVANDERIA ---")
        print("1 - Adicionar pedido")
        print("2 - Listar pedidos")
        print("3 - Atualizar status")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            adicionar_pedido()
        elif opcao == "2":
            listar_pedidos()
        elif opcao == "3":
            atualizar_status()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")


# -------------------------------
# Execução
# -------------------------------
if __name__ == "__main__":
    menu()
    
import csv
import os

ARQUIVO = "pedidos.csv"
CABECALHO = ["cliente", "servico", "valor", "status"]


def validar_valor(valor):
    try:
        float(valor)
        return True
    except ValueError:
        return False


def inicializar_arquivo():
    if not os.path.exists(ARQUIVO) or os.path.getsize(ARQUIVO) == 0:
        with open(ARQUIVO, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(CABECALHO)


def ler_pedidos():
    inicializar_arquivo()

    with open(ARQUIVO, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        pedidos = []

        for linha in reader:
            if not linha:
                continue

            if [coluna.strip().lower() for coluna in linha[:4]] == CABECALHO:
                continue

            if len(linha) < 4:
                continue

            pedidos.append(linha[:4])

    return pedidos


def salvar_pedidos(pedidos):
    with open(ARQUIVO, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(CABECALHO)
        writer.writerows(pedidos)


def adicionar_pedido():
    inicializar_arquivo()

    cliente = input("Nome do cliente: ").strip()
    servico = input("Servico: ").strip()

    while True:
        valor = input("Valor: ").strip()
        if validar_valor(valor):
            break
        print("Valor invalido! Digite apenas numeros.")

    with open(ARQUIVO, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([cliente, servico, valor, "Em andamento"])

    print("Pedido adicionado com sucesso!")


def listar_pedidos():
    pedidos = ler_pedidos()

    if not pedidos:
        print("\nNenhum pedido cadastrado.")
        return

    print("\nPEDIDOS:\n")
    for i, linha in enumerate(pedidos, start=1):
        print(f"{i}. Cliente: {linha[0]}")
        print(f"   Servico: {linha[1]}")
        print(f"   Valor: R$ {linha[2]}")
        print(f"   Status: {linha[3]}")
        print("-" * 30)


def atualizar_status():
    pedidos = ler_pedidos()

    if not pedidos:
        print("Nenhum pedido encontrado.")
        return

    listar_pedidos()

    try:
        indice = int(input("Numero do pedido: ").strip()) - 1
    except ValueError:
        print("Digite um numero valido.")
        return

    if indice < 0 or indice >= len(pedidos):
        print("Pedido invalido.")
        return

    novo_status = input("Novo status: ").strip()
    if not novo_status:
        print("O status nao pode ficar vazio.")
        return

    pedidos[indice][3] = novo_status
    salvar_pedidos(pedidos)
    print("Status atualizado!")


def menu():
    while True:
        print("\n--- SISTEMA LAVANDERIA ---")
        print("1 - Adicionar pedido")
        print("2 - Listar pedidos")
        print("3 - Atualizar status")
        print("4 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "1":
            adicionar_pedido()
        elif opcao == "2":
            listar_pedidos()
        elif opcao == "3":
            atualizar_status()
        elif opcao == "4":
            print("Saindo...")
            break
        else:
            print("Opcao invalida!")


if __name__ == "__main__":
    menu()