from cli_pedidos import database
from cli_pedidos.models import Pedido


def test_inserir_e_listar_pedido(tmp_path):
    caminho_banco = str(tmp_path / "teste.db")
    database.inicializar_banco(caminho_banco)

    pedido = Pedido(cliente="Ana", servico="Lavagem", valor=50.0)
    pedido_inserido = database.inserir_pedido(caminho_banco, pedido)

    assert pedido_inserido.id is not None
    assert pedido_inserido.status == "Em andamento"
    assert pedido_inserido.criado_em is not None

    pedidos = database.listar_pedidos(caminho_banco)
    assert len(pedidos) == 1
    assert pedidos[0].cliente == "Ana"


def test_buscar_por_cliente(tmp_path):
    caminho_banco = str(tmp_path / "teste.db")
    database.inicializar_banco(caminho_banco)
    database.inserir_pedido(
        caminho_banco, Pedido(cliente="Ana Souza", servico="Lavagem", valor=50.0)
    )
    database.inserir_pedido(
        caminho_banco, Pedido(cliente="Bruno Lima", servico="Secagem", valor=30.0)
    )

    resultado = database.buscar_pedidos(caminho_banco, cliente="ana")

    assert len(resultado) == 1
    assert resultado[0].cliente == "Ana Souza"


def test_buscar_por_status(tmp_path):
    caminho_banco = str(tmp_path / "teste.db")
    database.inicializar_banco(caminho_banco)
    p1 = database.inserir_pedido(
        caminho_banco, Pedido(cliente="Ana", servico="Lavagem", valor=50.0)
    )
    database.inserir_pedido(
        caminho_banco, Pedido(cliente="Bruno", servico="Secagem", valor=30.0)
    )
    database.atualizar_status(caminho_banco, p1.id, "Concluido")

    resultado = database.buscar_pedidos(caminho_banco, status="Concluido")

    assert len(resultado) == 1
    assert resultado[0].cliente == "Ana"


def test_atualizar_status_existente(tmp_path):
    caminho_banco = str(tmp_path / "teste.db")
    database.inicializar_banco(caminho_banco)
    pedido = database.inserir_pedido(
        caminho_banco, Pedido(cliente="Ana", servico="Lavagem", valor=50.0)
    )

    resultado = database.atualizar_status(caminho_banco, pedido.id, "Concluido")

    assert resultado is True
    pedidos = database.listar_pedidos(caminho_banco)
    assert pedidos[0].status == "Concluido"


def test_atualizar_status_inexistente(tmp_path):
    caminho_banco = str(tmp_path / "teste.db")
    database.inicializar_banco(caminho_banco)

    resultado = database.atualizar_status(caminho_banco, 999, "Concluido")

    assert resultado is False


def test_excluir_pedido_existente(tmp_path):
    caminho_banco = str(tmp_path / "teste.db")
    database.inicializar_banco(caminho_banco)
    pedido = database.inserir_pedido(
        caminho_banco, Pedido(cliente="Ana", servico="Lavagem", valor=50.0)
    )

    resultado = database.excluir_pedido(caminho_banco, pedido.id)

    assert resultado is True
    assert database.listar_pedidos(caminho_banco) == []


def test_excluir_pedido_inexistente(tmp_path):
    caminho_banco = str(tmp_path / "teste.db")
    database.inicializar_banco(caminho_banco)

    resultado = database.excluir_pedido(caminho_banco, 999)

    assert resultado is False


def test_relatorio_com_multiplos_pedidos(tmp_path):
    caminho_banco = str(tmp_path / "teste.db")
    database.inicializar_banco(caminho_banco)
    p1 = database.inserir_pedido(
        caminho_banco, Pedido(cliente="Ana", servico="Lavagem", valor=50.0)
    )
    database.inserir_pedido(
        caminho_banco, Pedido(cliente="Bruno", servico="Secagem", valor=30.0)
    )
    database.atualizar_status(caminho_banco, p1.id, "Concluido")

    dados = database.relatorio(caminho_banco)

    assert dados["total_faturado"] == 80.0
    assert dados["por_status"] == {"Concluido": 1, "Em andamento": 1}
