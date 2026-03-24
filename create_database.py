import sqlite3

# Conecta o banco de dados
conn = sqlite3.connect("jogos.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    jogo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTEGER NOT NULL,
    preco REAL,
    data_cadastro DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

print("Banco de dados e tabela criados com sucesso!")

# Salvar alterações e fechar conexão com o banco  
conn.commit()
conn.close()
