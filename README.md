<div align="center">

![Header](https://capsule-render.vercel.app/api?type=wave&color=555555&height=120&section=header&text=CLI+Pedidos&fontSize=36&fontColor=ffffff)

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat&logo=python)
![Status](https://img.shields.io/badge/Status-Conclu%C3%ADdo-555?style=flat)

</div>

---

## O que é

CLI Pedidos é uma aplicação de linha de comando escrita em Python para gerenciar pedidos de serviços de lavanderia. O sistema permite registrar, listar e atualizar o status de pedidos diretamente pelo terminal, sem depender de banco de dados externo.

A persistência dos dados é feita em um arquivo CSV criado automaticamente na primeira execução, tornando o projeto leve e autossuficiente — basta ter o Python instalado para rodar.

---

## Tech Stack

[![Skills](https://skillicons.dev/icons?i=python)](https://skillicons.dev)

> Utiliza apenas a biblioteca padrão do Python (`csv`) — sem dependências externas.

---

## Como Rodar

```bash
git clone https://github.com/Liraas-v/CLI-PEDIDOS
cd CLI-PEDIDOS

python app.py
```

> O arquivo `pedidos.csv` é criado automaticamente na primeira execução com os cabeçalhos corretos.

---

## Funcionalidades

- Registro de pedidos com cliente, tipo de serviço, valor e status automático "Em andamento"
- Listagem formatada de todos os pedidos cadastrados
- Atualização de status de pedidos existentes
- Criação automática do arquivo CSV com cabeçalhos na primeira execução
- Validação dos dados de entrada
- Tratamento de exceções e dados inválidos

---

## O que aprendi

- Manipulação de arquivos CSV com o módulo nativo do Python
- Organização do código em funções para melhorar a modularidade e legibilidade
- Validação de dados de entrada e tratamento de exceções em aplicações CLI
- Persistência simples de dados sem dependências externas
- Boas práticas de estruturação de projetos Python pequenos
- Base para evolução do projeto em direção a sistemas web com frameworks como Flask

<div align="center">

![Footer](https://capsule-render.vercel.app/api?type=wave&color=555555&height=80&section=footer)

</div>
