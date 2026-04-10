# 🚀 To-Do API

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como parte da disciplina de Engenharia de Software, com o objetivo de implementar um pipeline completo de CI/CD utilizando GitHub Actions. A aplicação consiste em uma API desenvolvida em Python, com testes automatizados e integração contínua para garantir qualidade, organização e automação no processo de desenvolvimento.

---

## 🎯 Objetivos

* Implementar testes automatizados
* Automatizar build e deploy
* Utilizar boas práticas de DevOps
* Garantir qualidade de software com CI/CD

---

## ⚙️ Tecnologias Utilizadas

* Python 3.11
* Pytest
* FastAPI
* Uvicorn
* GitHub Actions

---

## 📁 Estrutura do Projeto

```
.
├── app/                    # Código fonte da aplicação
├── tests/                  # Testes automatizados
├── scripts/                # Scripts auxiliares
├── requirements.txt        # Dependências do projeto
├── README.md               # Documentação
├── LICENSE                 # Licença utilizada no projeto
└── .github/workflows/      # Pipeline CI/CD
```

---

## 🧪 Testes Automatizados

Os testes foram implementados utilizando Pytest e cobrem:

* ✅ Casos de uso principais (fluxo normal)
* ❌ Casos de erro (fluxo de exceção)

Total:

* 10 testes de fluxo normal
* 10 testes de exceção

### 📊 Relatórios gerados:

* Relatório HTML dos testes
* Relatório de cobertura de código

---

## 🔄 Pipeline CI/CD

O pipeline foi implementado com GitHub Actions e é composto por 4 jobs:

### 🧪 1. Test

* Instala dependências
* Executa testes automatizados
* Gera relatórios
* Salva artifacts

### 📦 2. Build

* Instala dependências
* Gera pacote `.zip` da aplicação
* Armazena como artifact

### 🚀 3. Deploy

* Executado apenas após sucesso de test e build
* Publica o artefato como release no GitHub

### 📧 4. Notify

* Executado após deploy
* Envia e-mail de notificação
* Utiliza variáveis de ambiente (secrets)

---

## 🔀 Execução do Pipeline

O pipeline é acionado automaticamente em:

* Push na branch `main`
* Pull requests para `main`

---

## 📦 Gerenciamento de Dependências

As dependências são gerenciadas via:

```
requirements.txt
```

E são instaladas automaticamente no pipeline com:

```
pip install -r requirements.txt
```

---

## 🔐 Variáveis de Ambiente

As seguintes variáveis são utilizadas no pipeline:

* SMTP_HOST
* SMTP_PORT
* EMAIL_USER
* EMAIL_PASS
* EMAIL_TO

Todas são configuradas como **GitHub Secrets**, garantindo segurança.

---

## 🚀 Deploy

O deploy consiste na publicação automática do build como release no GitHub.

* Ele é executado somente após sucesso dos testes e build
* Geração de versão baseada no número da execução

---

## 👥 Integrantes

* Antonio Alexandre Barbosa da Silva
* Bianca Ribeiro de Souza

---

## 🤖 Uso de Inteligência Artificial

Este projeto utilizou ferramentas de IA como apoio para:

* Estruturação do pipeline CI/CD
* Revisão de boas práticas
* Sugestões de melhoria

Todos os resultados foram revisados e adaptados manualmente pelo grupo.

---

## 📌 Como Executar Localmente

1. Clone o repositório, HTTPS ou SSH:

```
git clone <URL_DO_REPOSITORIO>
```

2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Execute a aplicação:

```
python main.py
```

4. Execute os testes:

```
python -m pytest
```
