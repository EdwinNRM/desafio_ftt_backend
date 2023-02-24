# API de gerenciamento de personagens
Esta é uma API básica para gerenciar personagens de uma empresa de animação. A API permite criar novos personagens ,listar os personagens existentes, atualizar as informações e deletar dados.

Pacotes
Para rodar a API os seguintes pacotes são necessários:

- Python 3.x
- Flask
- Flask SQLAlchemy
- SQLAlchemy
- PyMySQL

Para executar a instação basta rodar o código a seguir:

$py pip install Flask Flask-SQLAlchemy PyMySQL


## Endpoints
### POST /characters/new
Cria um novo personagem com as informações fornecidas no corpo da requisição.

Parâmetros:
- nome: Nome do personagem (string, obrigatório)
- descricao: Descrição do personagem (string, obrigatório)
- imagem: Link para a imagem do personagem (string, obrigatório)
- programa: Nome do programa em que o personagem aparece (string, obrigatório)
- animador: Nome do animador responsável pelo personagem (string, obrigatório)

Exemplo de requisição json
```
 {
  "nome": "The_Godwin",
  "descricao": "Um grande programador back end e preferido do professor henrique",
  "imagem": "https://media.discordapp.net/attachments/1073046735162720327/1073046814003052544/ME.png",
  "programa": "Aluno",
  "animador": "Edwin Medina"
  }
```
Resposta json
```
{
  "msg": "The_Godwin criado com sucesso!"
}
```
### GET /characters
Lista todos os personagens existentes.

Resposta json
```
[
  {
    "id": 1,
    "nome": "The_Godwin",
    "descricao": "Um grande programador back end e preferido do professor henrique",
    "imagem": "https://media.discordapp.net/attachments/1073046735162720327/1073046814003052544/ME.png",
    "programa": "Aluno",
    "animador": "Edwin Medina"
  }

  {
    "id": 2,
    "nome": "Aluno estudioso",
    "descricao": "Figura lendária e de difícil visualização nos tempos atuais!",
    "imagem": "noimage",
    "programa": "Aluno",
    "animador": "Edwin Medina"
  }
]
```

### GET /characters/$id
Lista o personsagem referente ao ID solicitado

Resposta json
```
[
  {
    "id": 1,
    "nome": "The_Godwin",
    "descricao": "Um grande programador back end e preferido do professor henrique",
    "imagem": "https://media.discordapp.net/attachments/1073046735162720327/1073046814003052544/ME.png",
    "programa": "Aluno",
    "animador": "Edwin Medina"
  }
]
```

### PUT /characters/$id
Atualiza um personagem com as informações fornecidas no corpo da requisição.

Parâmetros:
- ID: ID de identificação do personagem a ser atualizado
- nome: Nome do personagem
- descricao: Descrição do personagem
- imagem: Link para a imagem do personagem
- programa: Nome do programa em que o personagem aparece
- animador: Nome do animador responsável pelo personagem

Exemplo de requisição json
```
{
  "nome": "The_Godwin",
  "descricao": "Um grande programador back end e preferido do professor henrique",
  "imagem": "https://media.discordapp.net/attachments/1073046735162720327/1073046814003052544/ME.png",
  "programa": "Aluno",
  "animador": "Edwin Medina"
}
```
Resposta json
```
{
  'msg': 'personagem atualizado com sucesso'
}
```
### DELETE /characters/$id
Deleta o personsagem referente ao ID solicitado
```
{
  'msg': 'personagem deletado com sucesso'
}
```
## Executando a aplicação
Para executar a aplicação utilize o seguinte comando no terminal:

$ py -m flask run

A aplicação estará disponível em "http://127.0.0.1:5000".
