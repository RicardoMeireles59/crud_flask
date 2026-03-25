<div align="center">

# 🎮 Games API

**Uma API RESTful para gerenciar sua coleção de jogos**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-FF6B6B?style=for-the-badge)

</div>

---

## 📖 Sobre o Projeto

API RESTful construída com **Python + Flask** para gerenciar uma coleção de jogos. Os dados são persistidos localmente em um banco de dados **SQLite**, com suporte completo às operações CRUD.

---

## 📁 Estrutura do Projeto

```
📦 games-api
 ┣ 📄 app.py               # Servidor principal com as rotas da API
 ┣ 📄 create_database.py   # Script de inicialização do banco de dados
 ┗ 🗄️  jogos.db             # Arquivo de banco de dados (gerado automaticamente)
```

---

## 🚀 Configuração e Instalação

### Pré-requisitos

- Python 3.x instalado

### 1️⃣ Instalar dependências

```bash
pip install flask
```

### 2️⃣ Criar e ativar o ambiente virtual

Isole as dependências do projeto com um ambiente virtual:

```bash
# Criar o ambiente virtual
python -m venv venv
```

```bash
# Ativar — Windows
venv\Scripts\activate

# Ativar — Linux / macOS
source venv/bin/activate
```

> ✅ Após a ativação, o terminal indicará que o ambiente virtual está em uso.

### 3️⃣ Inicializar o banco de dados

Cria a tabela `jogos` com as colunas: `id`, `jogo`, `autor`, `ano`, `preço` e `data_cadastro`.

```bash
python create_database.py
```

### 4️⃣ Iniciar o servidor

```bash
python app.py
```

> 🌐 O servidor estará disponível em **http://127.0.0.1:5000**

---

## 📡 Endpoints da API

Use ferramentas como **Postman**, **Insomnia** ou o próprio navegador para interagir com a API.

| Método | Rota | Descrição |
|--------|------|-----------|
| `GET` | `/jogos` | Lista todos os jogos |
| `GET` | `/jogos/<id>` | Busca um jogo pelo ID |
| `POST` | `/adicionarjogo` | Adiciona um novo jogo |
| `PUT` | `/jogos/<id>` | Atualiza um jogo existente |
| `DELETE` | `/jogos/<id>` | Remove um jogo da coleção |

---

### 🔍 Exemplos de Uso

<details>
<summary><b>GET /jogos</b> — Listar todos os jogos</summary>

```http
GET http://127.0.0.1:5000/jogos
```

</details>

<details>
<summary><b>GET /jogos/&lt;id&gt;</b> — Buscar um jogo específico</summary>

```http
GET http://127.0.0.1:5000/jogos/1
```

</details>

<details>
<summary><b>POST /adicionarjogo</b> — Adicionar um novo jogo</summary>

```http
POST http://127.0.0.1:5000/adicionarjogo
Content-Type: application/json
```

```json
{
  "jogo": "God of War",
  "autor": "David Jaffe",
  "ano": 2005,
  "preco": 99.99
}
```

</details>

<details>
<summary><b>PUT /jogos/&lt;id&gt;</b> — Atualizar um jogo</summary>

```http
PUT http://127.0.0.1:5000/jogos/1
Content-Type: application/json
```

```json
{
  "jogo": "God of War",
  "autor": "David Jaffe",
  "ano": 2005,
  "preco": 79.99
}
```

</details>

<details>
<summary><b>DELETE /jogos/&lt;id&gt;</b> — Remover um jogo</summary>

```http
DELETE http://127.0.0.1:5000/jogos/1
```

</details>

---

## 🛠️ Detalhes Técnicos

- **Banco de Dados:** SQLite3 — arquivo local `jogos.db`
- **Persistência:** Dados salvos diretamente no arquivo de banco de dados
- **Tratamento de Erros:** Respostas amigáveis com `404` para recursos não encontrados

---

<div align="center">

Feito com ❤️ e ☕

</div>
