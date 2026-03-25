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

# Roteiro de Testes — API Flask de Jogos

Testes manuais utilizando `curl` para validar todos os endpoints da API.

> **Pré-requisito:** servidor Flask rodando em `http://127.0.0.1:5000`

---

## GET — Listar todos os jogos

Retorna um array JSON com todos os registros cadastrados.

```bash
curl -X GET http://127.0.0.1:5000/jogos \
  -H "Content-Type: application/json"
```

**Resposta esperada:** `200 OK`

```json
[
  {
    "id": 1,
    "jogo": "The Last of Us",
    "autor": "Naughty Dog",
    "ano": 2013,
    "preco": 149.9,
    "data_cadastro": "2024-01-01"
  }
]
```

---

## GET — Buscar jogo por ID (encontrado)

Retorna um único registro pelo ID informado.

```bash
curl -X GET http://127.0.0.1:5000/jogos/1 \
  -H "Content-Type: application/json"
```

**Resposta esperada:** `200 OK`

```json
{
  "id": 1,
  "jogo": "The Last of Us",
  "autor": "Naughty Dog",
  "ano": 2013,
  "preco": 149.9,
  "data_cadastro": "2024-01-01"
}
```

---

## GET — Buscar jogo por ID (não encontrado)

Deve retornar erro quando o ID não existe no banco.

```bash
curl -X GET http://127.0.0.1:5000/jogos/9999 \
  -H "Content-Type: application/json"
```

**Resposta esperada:** `404 Not Found`

```json
{
  "erro": "Jogo não encontrado"
}
```

---

## POST — Adicionar novo jogo

Insere um novo registro no banco de dados.

```bash
curl -X POST http://127.0.0.1:5000/adicionarjogo \
  -H "Content-Type: application/json" \
  -d '{
    "jogo": "The Last of Us",
    "autor": "Naughty Dog",
    "ano": 2013,
    "preco": 149.90
  }'
```

**Resposta esperada:** `201 Created`

```json
{
  "mensagem": "Jogo adicionado com sucesso!"
}
```

---

## PUT — Atualizar jogo por ID (encontrado)

Altera todos os campos de um registro existente.

```bash
curl -X PUT http://127.0.0.1:5000/jogos/1 \
  -H "Content-Type: application/json" \
  -d '{
    "jogo": "The Last of Us Part I",
    "autor": "Naughty Dog",
    "ano": 2022,
    "preco": 249.90
  }'
```

**Resposta esperada:** `200 OK`

```json
{
  "mensagem": "Jogo atualizado com sucesso!"
}
```

---

## PUT — Atualizar jogo por ID (não encontrado)

Deve retornar erro quando o ID informado não existe.

```bash
curl -X PUT http://127.0.0.1:5000/jogos/9999 \
  -H "Content-Type: application/json" \
  -d '{
    "jogo": "Inexistente",
    "autor": "Ninguém",
    "ano": 2000,
    "preco": 0
  }'
```

**Resposta esperada:** `404 Not Found`

```json
{
  "erro": "Jogo não encontrado"
}
```

---

## DELETE — Remover jogo por ID (encontrado)

Exclui o registro e confirma com o nome do jogo removido.

```bash
curl -X DELETE http://127.0.0.1:5000/jogos/1 \
  -H "Content-Type: application/json"
```

**Resposta esperada:** `200 OK`

```json
{
  "mensagem": "Jogo 'The Last of Us' removido!"
}
```

---

## DELETE — Remover jogo por ID (não encontrado)

Deve retornar erro quando o ID não existe no banco.

```bash
curl -X DELETE http://127.0.0.1:5000/jogos/9999 \
  -H "Content-Type: application/json"
```

**Resposta esperada:** `404 Not Found`

```json
{
  "erro": "Jogo não encontrado"
}
```

---

## 🛠️ Detalhes Técnicos

- **Banco de Dados:** SQLite3 — arquivo local `jogos.db`
- **Persistência:** Dados salvos diretamente no arquivo de banco de dados
- **Tratamento de Erros:** Respostas amigáveis com `404` para recursos não encontrados

---

<div align="center">

Feito com ❤️ e ☕

</div>
