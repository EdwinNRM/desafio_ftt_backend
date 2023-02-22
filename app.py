from flask import Flask, request, jsonify

app = Flask(__name__)

personagens = []

# Endpoint para criação de personagens
@app.route('/characters/', methods=['POST'])
def criar_personagem():
    novo_personagem = {
        'nome': request.json['nome'],
        'descricao': request.json['descricao'],
        'imagem': request.json['imagem'],
        'programa': request.json['programa'],
        'animador': request.json['animador']
    }
    personagens.append(novo_personagem)
    return jsonify({'mensagem': 'Personagem criado com sucesso!'})

# Endpoint para recuperação de personagens
@app.route('/characters/', methods=['GET'])
def listar_personagens():
    return jsonify(personagens)

if __name__ == '__main__':
    app.run(debug=True)
