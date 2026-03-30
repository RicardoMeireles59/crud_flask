from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jogos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Criação do modelo de ORM
class Jogo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jogo = db.Column(db.String(100), nullable=False)
    autor = db.Column(db.String(100))
    ano = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)

# Criação automática das tabelas
with app.app_context():
    db.create_all()

# GET 
@app.route('/jogos', methods=['GET'])
@app.route('/jogos/<int:id>', methods=['GET'])
def gerenciar_jogos(id=None):

    # Busca por ID usando ORM
    if id:
        jogo = Jogo.query.get(id)

        if jogo:
            return jsonify({
                "id": jogo.id,
                "jogo": jogo.jogo,
                "autor": jogo.autor,
                "ano": jogo.ano,
                "preco": jogo.preco,
            }), 200

        return jsonify({"erro": "Jogo não encontrado"}), 404

    # Listagem usando ORM
    jogos = Jogo.query.all()

    lista_jogos = [{
        "id": j.id,
        "jogo": j.jogo,
        "autor": j.autor,
        "ano": j.ano,
        "preco": j.preco,
    } for j in jogos]

    return jsonify(lista_jogos), 200


# POST 
@app.route('/insert', methods=['POST'])
def criar_jogo():
    dados = request.get_json()

    # Inserção de registro usando ORM
    novo_jogo = Jogo(
        jogo = dados.get('jogo'),
        autor = dados.get('autor'),
        ano = dados.get('ano'),
        preco = dados.get('preco')
    )

    db.session.add(novo_jogo)
    db.session.commit()

    return jsonify({"mensagem": "Jogo criado com sucesso!"}), 201


# PUT 
@app.route('/update/<int:id>', methods=['PUT'])
def atualizar_jogo(id):
    dados = request.get_json()

    jogo = Jogo.query.get(id)
    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    # Alteração de registro usando ORM

    jogo.jogo = dados.get('jogo')
    jogo.autor = dados.get('autor')
    jogo.ano = dados.get('ano')
    jogo.preco = dados.get('preco')

    db.session.commit()

    return jsonify({"mensagem": "Jogo atualizado com sucesso!"}), 200

# DELETE
@app.route('/delete/<int:id>', methods=['DELETE'])
def deletar_jogo(id):
    jogo = Jogo.query.get(id)

    if not jogo:
        return jsonify({"erro": "Jogo não encontrado"}), 404

    # Eliminação de registro usando ORM

    db.session.delete(jogo)
    db.session.commit()

    return jsonify({"mensagem": f"Jogo '{jogo.jogo}' removido!"}), 200

if __name__ == '__main__':
    app.run(debug=True)