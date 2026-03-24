from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def executar_query(query, *args, fetch=False, commit=False):
    conn = sqlite3.connect('jogos.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    resultado = None
    
    try:
        cursor.execute(query, args)
        
        if commit:
            conn.commit()
        if fetch:
            resultado = cursor.fetchall()
    finally:
        conn.close()
    
    return resultado

""" GET (Listar Todos): Retornar uma lista JSON de todos os registros.GET (Buscar por ID): Retornar apenas um registro específico ou erro 404. """

@app.route('/jogos', methods=['GET'])
@app.route('/jogos/<int:id>', methods=['GET'])

def buscar_jogo(id=None):
    if id:
        jogo = executar_query("SELECT * FROM jogos WHERE id = ? ", id, fetch=True)
        if jogo: 
            return jsonify(dict(jogo[0])), 200 
        return jsonify({"erro": "Jogo não encontrado"}), 404

    jogo = executar_query("SELECT id, jogo, autor, ano, preco, data_cadastro FROM jogos", fetch=True)
    lista_jogos = [dict(item) for item in jogo]
    return jsonify(lista_jogos), 200

"""POST (Inserir): Receber um JSON e salvar no banco (com status 201).""" 
 
@app.route('/adicionarjogo', methods=['POST'])

def adicionar_jogo():
    jogos = request.get_json()

    executar_query(
        "INSERT INTO jogos (jogo, autor, ano, preco ) VALUES (?, ?, ?, ?)",
        
            jogos.get('jogo'), 
            jogos.get('autor'), 
            jogos.get('ano'), 
            jogos.get('preco'), 
            commit=True
    )
    return jsonify({"mensagem": "Jogo adicionado com sucesso!"}), 201

"""PUT (Atualizar): Alterar dados de um registro existente via ID (status 204). """

@app.route('/jogos/<int:id>', methods=['PUT'])
def atualizar_jogo(id): 
    dados = request.get_json()
    
    existe = executar_query(
        "SELECT id FROM jogos WHERE id = ?",
        id,
        fetch=True
    )

    if not existe:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query(
        "UPDATE jogos SET jogo = ?, autor = ?, ano = ?, preco = ? WHERE id = ?",
            dados.get('jogo'), 
            dados.get('autor'), 
            dados.get('ano'),
            dados.get('preco'), 
            id,
            commit=True
    )

    return jsonify({"mensagem": "Jogo atualizado com sucesso!"}), 200

""" DELETE (Remover): Excluir um registro do banco via ID. """

@app.route('/jogos/<int:id>', methods=['DELETE'])

def deletar_jogo(id):
    jogo = executar_query("SELECT jogo FROM jogos WHERE id = ?", id, fetch=True)
    
    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    executar_query("DELETE FROM jogos WHERE id = ?", id, commit=True)
    return jsonify({"mensagem": f"Jogo '{jogo[0]['jogo']}' removido!"}), 200

if __name__ == '__main__': 
    app.run(debug=True)

