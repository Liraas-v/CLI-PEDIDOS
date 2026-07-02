import sqlite3
from datetime import datetime, timezone
from typing import Optional

from .models import Pedido


def inicializar_banco(caminho_banco: str) -> None:
    conexao = sqlite3.connect(caminho_banco)
    try:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS pedidos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                cliente TEXT NOT NULL,
                servico TEXT NOT NULL,
                valor REAL NOT NULL,
                status TEXT NOT NULL DEFAULT 'Em andamento',
                criado_em TEXT NOT NULL
            )
            """
        )
        conexao.commit()
    finally:
        conexao.close()


def inserir_pedido(caminho_banco: str, pedido: Pedido) -> Pedido:
    criado_em = pedido.criado_em or datetime.now(timezone.utc).isoformat()
    conexao = sqlite3.connect(caminho_banco)
    try:
        cursor = conexao.execute(
            """
            INSERT INTO pedidos (cliente, servico, valor, status, criado_em)
            VALUES (?, ?, ?, ?, ?)
            """,
            (pedido.cliente, pedido.servico, pedido.valor, pedido.status, criado_em),
        )
        conexao.commit()
        novo_id = cursor.lastrowid
    finally:
        conexao.close()

    return Pedido(
        id=novo_id,
        cliente=pedido.cliente,
        servico=pedido.servico,
        valor=pedido.valor,
        status=pedido.status,
        criado_em=criado_em,
    )


def _linha_para_pedido(linha) -> Pedido:
    id_, cliente, servico, valor, status, criado_em = linha
    return Pedido(
        id=id_,
        cliente=cliente,
        servico=servico,
        valor=valor,
        status=status,
        criado_em=criado_em,
    )


def listar_pedidos(caminho_banco: str) -> list[Pedido]:
    conexao = sqlite3.connect(caminho_banco)
    try:
        linhas = conexao.execute(
            "SELECT id, cliente, servico, valor, status, criado_em "
            "FROM pedidos ORDER BY id"
        ).fetchall()
    finally:
        conexao.close()
    return [_linha_para_pedido(linha) for linha in linhas]


def buscar_pedidos(
    caminho_banco: str,
    cliente: Optional[str] = None,
    status: Optional[str] = None,
) -> list[Pedido]:
    condicoes = []
    parametros: list = []

    if cliente:
        condicoes.append("LOWER(cliente) LIKE ?")
        parametros.append(f"%{cliente.lower()}%")

    if status:
        condicoes.append("status = ?")
        parametros.append(status)

    sql = "SELECT id, cliente, servico, valor, status, criado_em FROM pedidos"
    if condicoes:
        sql += " WHERE " + " AND ".join(condicoes)
    sql += " ORDER BY id"

    conexao = sqlite3.connect(caminho_banco)
    try:
        linhas = conexao.execute(sql, parametros).fetchall()
    finally:
        conexao.close()
    return [_linha_para_pedido(linha) for linha in linhas]


def atualizar_status(caminho_banco: str, id_pedido: int, novo_status: str) -> bool:
    conexao = sqlite3.connect(caminho_banco)
    try:
        cursor = conexao.execute(
            "UPDATE pedidos SET status = ? WHERE id = ?", (novo_status, id_pedido)
        )
        conexao.commit()
    finally:
        conexao.close()
    return cursor.rowcount > 0


def excluir_pedido(caminho_banco: str, id_pedido: int) -> bool:
    conexao = sqlite3.connect(caminho_banco)
    try:
        cursor = conexao.execute("DELETE FROM pedidos WHERE id = ?", (id_pedido,))
        conexao.commit()
    finally:
        conexao.close()
    return cursor.rowcount > 0


def relatorio(caminho_banco: str) -> dict:
    conexao = sqlite3.connect(caminho_banco)
    try:
        total_faturado = conexao.execute(
            "SELECT COALESCE(SUM(valor), 0) FROM pedidos"
        ).fetchone()[0]
        linhas_status = conexao.execute(
            "SELECT status, COUNT(*) FROM pedidos GROUP BY status"
        ).fetchall()
    finally:
        conexao.close()
    return {
        "total_faturado": total_faturado,
        "por_status": dict(linhas_status),
    }
