from flask import Flask,jsonify, request
from flask_restx import Resource, Api, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app, version='1.0', title='Character API',
    description='A simple CRUD API for Turing Technology Factory')

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

    def __init__(self, nome, descricao, imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.programa = programa
        self.animador = animador

db.init_app(app)

with app.app_context():
    db.create_all()

character_model = api.model('Character', {
    'nome': fields.String(required=True, description='The character name'),
    'descricao': fields.String(required=True, description='The character description'),
    'imagem': fields.String(required=True, description='The character image URL'),
    'programa': fields.String(required=True, description='The character show'),
    'animador': fields.String(required=True, description='The character creator')
})

@api.route('/characters')
class GpCharacter(Resource):
    @api.expect(character_model)
    def post(self):
        ''' Create a character '''
        data = request.json
        new_character = Characters(nome=data['nome'], descricao=data['descricao'], imagem=data['imagem'], programa=data['programa'], animador=data['animador'])
        db.session.add(new_character)
        db.session.commit()
        return jsonify({'msg': new_character.nome +' created successfully!'})

    def get(self):
        ''' Get all characters'''
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

@api.route('/characters/<int:id>')
class CharactersById (Resource):
    @api.doc(params={'id': 'The character ID'})
    def get(self, id):
        ''' Get a character'''
        character = Characters.query.get(id)
        if character is None:
            return jsonify({'error': 'Character not found'}), 404
        character_data = {
            'id': character.id,
            'nome': character.nome,
            'descricao': character.descricao,
            'imagem': character.imagem,
            'programa': character.programa,
            'animador': character.animador
        }
        return jsonify(character_data)

    @api.doc(params={'id': 'ID of the character'})
    @api.expect(character_model)
    def put(self, id):
        '''Update a character by ID'''
        character = Characters.query.get(id)
        if character is None:
            return {'error': 'Character not found'}, 404
        data = api.payload
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
        return {'msg': 'Character updated successfully'}

    @api.doc(params={'id': 'ID of the character'})
    def delete(self, id):
        '''Delete a character by ID'''
        character = Characters.query.get(id)
        if character is None:
            return {'error': 'Character not found'}, 404
        db.session.delete(character)
        db.session.commit()
        return {'msg': 'Character deleted successfully'}
        
if __name__ == '__main__':
    app.run(debug = True)