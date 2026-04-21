# 📦 Sistema de Pedidos - Lavanderia (CLI)

## 📌 Sobre o projeto

Este projeto é um sistema de linha de comando (CLI) desenvolvido em Python para gerenciamento de pedidos de uma lavanderia.

A aplicação permite cadastrar, visualizar e atualizar pedidos de forma simples, utilizando um arquivo CSV como armazenamento.

O foco do projeto é aplicar conceitos fundamentais de desenvolvimento, como organização de código, validação de dados e persistência.

---

## 🚀 Funcionalidades

* Cadastro de pedidos com:

  * Cliente
  * Serviço
  * Valor
  * Status automático ("Em andamento")

* Listagem de pedidos formatada

* Atualização de status de pedidos

* Criação automática do arquivo `pedidos.csv`

* Validação de entrada de dados

---

## 🛠 Tecnologias utilizadas

* Python 3
* Bibliotecas padrão:

  * csv
  * os

---

## 📂 Estrutura do projeto

```
lavanderia_cli/
│
├── app.py
├── pedidos.csv
└── README.md
```

---

## ▶️ Como executar

### 1. Clonar o repositório

```
git clone https://github.com/Liraas-v/CLI-PEDIDOS.git
```
### 2. Executar o sistema

```
python app.py
```

---

## 🧾 Funcionamento

Ao iniciar o sistema:

* O arquivo `pedidos.csv` é criado automaticamente (caso não exista)
* O sistema garante que o cabeçalho esteja correto
* Dados inválidos são tratados (ex: valor não numérico)

---

## 💻 Exemplo de uso

```
--- SISTEMA LAVANDERIA ---
1 - Adicionar pedido
2 - Listar pedidos
3 - Atualizar status
4 - Sair
```

---

## 🧠 Conceitos aplicados

* Manipulação de arquivos CSV
* Estruturação em funções
* Validação de dados
* Tratamento de exceções
* Separação de responsabilidades
* Persistência simples de dados

---

## 📊 Diferenciais técnicos

* Inicialização automática do arquivo de dados
* Tratamento de inconsistências no CSV
* Código modular e organizado
* Base preparada para evolução para aplicações web (Flask)

---

## 🎯 Objetivo

Este projeto faz parte de um portfólio com foco em evolução prática em Python, servindo como base para sistemas mais avançados, como APIs e aplicações web.

---

## 👨‍💻 Autor

Desenvolvido por você 🚀
