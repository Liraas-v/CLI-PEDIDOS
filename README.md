<div align="center">

# CLI Pedidos

CLI para gerenciar pedidos de uma lavanderia, direto pelo terminal.

[![Skills](https://skillicons.dev/icons?i=python,sqlite,github)](https://skillicons.dev)

</div>

---

## O que é

CLI Pedidos é uma aplicação de linha de comando escrita em Python para
gerenciar pedidos de servicos de lavanderia: cadastrar, listar, buscar,
atualizar status, excluir e gerar um relatorio de faturamento.

A persistencia dos dados é feita em SQLite (`pedidos.db`), criado
automaticamente na primeira execução — nenhuma dependencia externa,
nenhum servidor de banco de dados necessário.

---

## Tech Stack

- Python 3.10+ (somente biblioteca padrão: `sqlite3`, `dataclasses`)
- SQLite como banco embutido
- `pytest` para testes automatizados
- GitHub Actions para integração contínua

---

## Arquitetura

```
src/cli_pedidos/
├── models.py      # dataclass Pedido
├── database.py     # camada de acesso ao SQLite (CRUD + relatório)
├── validators.py    # validação de entrada
├── cli.py         # menu interativo
└── __main__.py      # ponto de entrada (python -m cli_pedidos)
```

Cada módulo tem uma responsabilidade única: `database.py` não sabe nada
sobre `input()`/`print()`, e `cli.py` não sabe nada sobre SQL — isso
permite testar as regras de negócio sem simular entrada de terminal.

---

## Como Rodar

```bash
git clone https://github.com/Liraas-v/CLI-PEDIDOS
cd CLI-PEDIDOS

pip install -e .
python -m cli_pedidos
```

> O arquivo `pedidos.db` é criado automaticamente na primeira execução.

---

## Funcionalidades

- Cadastro de pedidos com cliente, serviço, valor e status automático
  "Em andamento"
- Listagem formatada de todos os pedidos, com ID e data de criação
- Busca/filtro por nome do cliente ou por status
- Atualização de status de pedidos existentes
- Exclusão de pedidos
- Relatório com faturamento total e quantidade de pedidos por status
- Validação de dados de entrada (valores numéricos positivos, campos
  obrigatórios)

---

## Como rodar os testes

```bash
pip install -e ".[dev]"
pytest -v
```

Os testes cobrem a camada de banco (`database.py`) e os validadores
(`validators.py`), cada um usando um banco SQLite temporário isolado —
nenhum teste toca o `pedidos.db` real.

---

## O que aprendi

- Separação de responsabilidades em um pacote Python (models, banco,
  validação, interface) em vez de um script único
- Persistência com SQLite via `sqlite3` da biblioteca padrão
- Testes automatizados com `pytest`, incluindo fixtures como `tmp_path`
  para isolar banco de dados em testes
- Empacotamento de projetos Python com `pyproject.toml` e `setuptools`
- Integração contínua com GitHub Actions
- Boas práticas de estruturação de projetos Python para além de scripts
  simples

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=wave&color=555555&height=80&section=footer)

</div>
