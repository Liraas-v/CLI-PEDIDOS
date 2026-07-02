from . import database
from .models import Pedido
from .validators import validar_texto_obrigatorio, validar_valor

CAMINHO_BANCO = "pedidos.db"


def _pedir_texto_obrigatorio(mensagem: str) -> str:
    while True:
        valor = input(mensagem).strip()
        if validar_texto_obrigatorio(valor):
            return valor
        print("Este campo nao pode ficar vazio.")


def _pedir_valor(mensagem: str) -> float:
    while True:
        texto = input(mensagem).strip()
        if validar_valor(texto):
            return float(texto)
        print("Valor invalido! Digite um numero maior que zero.")


def _exibir_pedido(indice: int, pedido: Pedido) -> None:
    print(f"{indice}. [ID {pedido.id}] Cliente: {pedido.cliente}")
    print(f"   Servico: {pedido.servico}")
    print(f"   Valor: R$ {pedido.valor:.2f}")
    print(f"   Status: {pedido.status}")
    print(f"   Criado em: {pedido.criado_em}")
    print("-" * 30)


def _exibir_lista(pedidos: list) -> None:
    if not pedidos:
        print("\nNenhum pedido encontrado.")
        return

    print("\nPEDIDOS:\n")
    for indice, pedido in enumerate(pedidos, start=1):
        _exibir_pedido(indice, pedido)


def adicionar_pedido() -> None:
    cliente = _pedir_texto_obrigatorio("Nome do cliente: ")
    servico = _pedir_texto_obrigatorio("Servico: ")
    valor = _pedir_valor("Valor: ")

    pedido = Pedido(cliente=cliente, servico=servico, valor=valor)
    database.inserir_pedido(CAMINHO_BANCO, pedido)
    print("Pedido adicionado com sucesso!")


def listar_pedidos() -> None:
    pedidos = database.listar_pedidos(CAMINHO_BANCO)
    _exibir_lista(pedidos)


def buscar_pedidos() -> None:
    cliente = input("Filtrar por cliente (Enter para ignorar): ").strip() or None
    status = input("Filtrar por status (Enter para ignorar): ").strip() or None
    pedidos = database.buscar_pedidos(CAMINHO_BANCO, cliente=cliente, status=status)
    _exibir_lista(pedidos)


def atualizar_status() -> None:
    pedidos = database.listar_pedidos(CAMINHO_BANCO)
    if not pedidos:
        print("Nenhum pedido cadastrado.")
        return

    _exibir_lista(pedidos)

    try:
        id_pedido = int(input("ID do pedido: ").strip())
    except ValueError:
        print("Digite um numero valido.")
        return

    novo_status = _pedir_texto_obrigatorio("Novo status: ")

    if database.atualizar_status(CAMINHO_BANCO, id_pedido, novo_status):
        print("Status atualizado!")
    else:
        print("Pedido nao encontrado.")


def excluir_pedido() -> None:
    pedidos = database.listar_pedidos(CAMINHO_BANCO)
    if not pedidos:
        print("Nenhum pedido cadastrado.")
        return

    _exibir_lista(pedidos)

    try:
        id_pedido = int(input("ID do pedido a excluir: ").strip())
    except ValueError:
        print("Digite um numero valido.")
        return

    if database.excluir_pedido(CAMINHO_BANCO, id_pedido):
        print("Pedido excluido!")
    else:
        print("Pedido nao encontrado.")


def exibir_relatorio() -> None:
    dados = database.relatorio(CAMINHO_BANCO)
    print("\nRELATORIO:\n")
    print(f"Faturamento total: R$ {dados['total_faturado']:.2f}")
    print("Pedidos por status:")
    if not dados["por_status"]:
        print("  Nenhum pedido cadastrado.")
    for status, quantidade in dados["por_status"].items():
        print(f"  {status}: {quantidade}")


def menu() -> None:
    database.inicializar_banco(CAMINHO_BANCO)

    opcoes = {
        "1": adicionar_pedido,
        "2": listar_pedidos,
        "3": buscar_pedidos,
        "4": atualizar_status,
        "5": excluir_pedido,
        "6": exibir_relatorio,
    }

    while True:
        print("\n--- SISTEMA LAVANDERIA ---")
        print("1 - Adicionar pedido")
        print("2 - Listar pedidos")
        print("3 - Buscar/filtrar pedidos")
        print("4 - Atualizar status")
        print("5 - Excluir pedido")
        print("6 - Relatorio")
        print("7 - Sair")

        opcao = input("Escolha: ").strip()

        if opcao == "7":
            print("Saindo...")
            break

        acao = opcoes.get(opcao)
        if acao is None:
            print("Opcao invalida!")
            continue

        acao()
