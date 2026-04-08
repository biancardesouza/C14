# To-Do API

## 📌 Descrição

Este projeto consiste em uma API REST simples para gerenciamento de tarefas, desenvolvida utilizando **FastAPI**. A aplicação permite criar, listar, atualizar, deletar e marcar tarefas como concluídas.

---

## 🚀 Tecnologias Utilizadas

* Python 3.x
* FastAPI
* Uvicorn

---

## 📂 Estrutura do Projeto

```
project/
│
├── app/
│   ├── main.py             # Ponto de entrada da aplicação
│   ├── models.py           # Modelos de dados
│   ├── service.py          # Regras de negócio
│   └── database.py         # Simulação de banco de dados em memória
│
├── requirements.txt
└── .gitignore
```

---

## ⚙️ Funcionalidades

A API oferece as seguintes operações:

* Criar uma tarefa
* Listar todas as tarefas
* Buscar uma tarefa por ID
* Atualizar uma tarefa
* Deletar uma tarefa
* Marcar uma tarefa como concluída

---

## 🌐 Endpoints

| Método | Rota                   | Descrição                      |
| ------ | ---------------------- | ------------------------------ |
| GET    | `/`                    | Verifica se a API está rodando |
| GET    | `/tasks`               | Lista todas as tarefas         |
| POST   | `/tasks`               | Cria uma nova tarefa           |
| GET    | `/tasks/{id}`          | Retorna uma tarefa específica  |
| PUT    | `/tasks/{id}`          | Atualiza uma tarefa            |
| DELETE | `/tasks/{id}`          | Remove uma tarefa              |
| PATCH  | `/tasks/{id}/complete` | Marca como concluída           |

---

## ▶️ Como Executar o Projeto

### 1. Clone o repositório

```bash
git clone https://github.com/biancardesouza/C14
cd C14
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute a aplicação

```bash
uvicorn app.main:app --reload
```

---

## 📖 Documentação interativa

Após iniciar o servidor, acesse:

```
http://127.0.0.1:8000/docs
```

A interface Swagger permite testar todos os endpoints diretamente pelo navegador.
