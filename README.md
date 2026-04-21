# 📦 Sistema de Pedidos - Lavanderia (CLI)

## 📌 Sobre o projeto

Este é um sistema simples de linha de comando (CLI) desenvolvido em Python para controle de pedidos de uma lavanderia.

O objetivo do projeto é resolver um problema real: organizar pedidos de clientes de forma prática, sem depender de papel ou anotações desorganizadas.

---

## 🚀 Funcionalidades

- ✅ Adicionar pedidos  
- ✅ Listar pedidos  
- ✅ Atualizar status dos pedidos  
- ✅ Armazenamento em arquivo `.csv`  

---

## 🛠 Tecnologias utilizadas

- Python 3  
- Biblioteca padrão `csv`  

---

## 📂 Estrutura do projeto

lavanderia_cli/
│
├── app.py
├── pedidos.csv
└── README.md

---

## ▶️ Como executar

### 1. Clonar o repositório
git clone https://github.com/seu-usuario/seu-repositorio.git

---

## 2. Acessar a pasta
cd lavanderia_cli

---

## 3. Executar o sistema
python app.py

---

## 🧾 Funcionamento

Ao iniciar o sistema:

- O arquivo `pedidos.csv` é criado automaticamente (caso não exista)
- O sistema garante que o cabeçalho esteja correto
- Dados inválidos são tratados (ex: valor não numérico)

---

## 💻 Exemplo de uso

--- SISTEMA LAVANDERIA ---
1 - Adicionar pedido
2 - Listar pedidos
3 - Atualizar status
4 - Sair


---

## 🧠 Conceitos aplicados

- Manipulação de arquivos CSV
- Estruturação em funções
- Validação de dados
- Tratamento de exceções
- Separação de responsabilidades
- Persistência simples de dados

---

## 📊 Diferenciais técnicos

- Inicialização automática do arquivo de dados
- Tratamento de inconsistências no CSV
- Código modular e organizado
- Base preparada para evolução para aplicações web (Flask)

---

## 🎯 Objetivo

Este projeto faz parte de um portfólio com foco em evolução prática em Python, servindo como base para sistemas mais avançados, como APIs e aplicações web.

---
