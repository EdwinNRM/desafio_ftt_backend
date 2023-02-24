from flask import Flask,jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234567@localhost/characters'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    imagem = db.Column(db.String(200), nullable=False)
    programa = db.Column(db.String(50), nullable=False)
    animador = db.Column(db.String(50), nullable=False)

    def __init__(self, nome, descricao, imagem, programa,animador):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.programa = programa
        self.animador = animador

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/new', methods=['POST'])
def create_character():
    data = request.json
    print(data)
    new_character = Characters(nome=data['nome'], descricao=data['descricao'], imagem=data['imagem'], programa=data['programa'], animador=data['animador'])
    db.session.add(new_character)
    db.session.commit()
    return jsonify({'msg': new_character.nome +' criado com sucesso!'})

@app.route('/characters', methods=['GET'])
def list_character():
    characters = Characters.query.all()
    output = []
    for character in characters:
        character_data = {}
        character_data['id'] = character.id
        character_data['nome'] = character.nome
        character_data['descricao'] = character.descricao
        character_data['imagem'] = character.imagem
        character_data['programa'] = character.programa
        character_data['animador'] = character.animador
        output.append(character_data)
    return jsonify({'characters': output})

@app.route('/characters/<int:id>', methods=['GET'])
def get_character(id):
    character = Characters.query.get(id)
    if character is None:
        return jsonify({'error': 'personagem não encontrado'}), 404
    character_data = {
        'id': character.id,
        'nome': character.nome,
        'descricao': character.descricao,
        'imagem': character.imagem,
        'programa': character.programa,
        'animador': character.animador
    }
    return jsonify(character_data)


@app.route('/characters/<int:id>', methods=['PUT'])
def update_character(id):
    character = Characters.query.get(id)
    if character is None:
        return jsonify({'error': 'personagem não encontrado'}), 404
    data = request.json
    if 'nome' in data:
        character.nome = data['nome']
    if 'descricao' in data:
        character.descricao = data['descricao']
    if 'imagem' in data:
        character.imagem = data['imagem']
    if 'programa' in data:
        character.programa = data['programa']
    if 'animador' in data:
        character.animador = data['animador']
    db.session.commit()
    return jsonify({'msg': 'personagem atualizado com sucesso'})

@app.route('/characters/<int:id>', methods=['DELETE'])
def delete_character(id):
    character = Characters.query.get(id)
    if character is None:
        return jsonify({'error': 'Character not found'}), 404
    db.session.delete(character)
    db.session.commit()
    return jsonify({'msg': 'personagem deletado com sucesso'})

if __name__ == '__main__':
    app.run(debug = True)