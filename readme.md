# API de gerenciamento de personagens
Esta é uma API básica para gerenciar personagens de uma empresa de animação. A API permite criar novos personagens e listar os personagens existentes.

## Endpoints
### POST /characters/
Cria um novo personagem com as informações fornecidas no corpo da requisição.

Parâmetros:
- nome: Nome do personagem (string, obrigatório)
- descricao: Descrição do personagem (string, obrigatório)
- imagem: Link para a imagem do personagem (string, obrigatório)
- programa: Nome do programa em que o personagem aparece (string, obrigatório)
- animador: Nome do animador responsável pelo personagem (string, obrigatório)

Exemplo de requisição json
 {
  "nome": "The_Godwin",
  "descricao": "Um grande programador back end e preferido do professor henrique",
  "imagem": "https://media.discordapp.net/attachments/1073046735162720327/1073046814003052544/ME.png",
  "programa": "Aluno",
  "animador": "Edwin Medina"
  }

Resposta json
{
"mensagem": "Personagem criado com sucesso!"
}

### GET /characters/
Lista todos os personagens existentes.

Resposta
json
[
  {
    "nome": "The_Godwin",
    "descricao": "Um grande programador back end e preferido do professor henrique",
    "imagem": "https://media.discordapp.net/attachments/1073046735162720327/1073046814003052544/ME.png",
    "programa": "Aluno",
    "animador": "Edwin Medina"
  }
]

## Executando a aplicação
Para executar a aplicação, é necessário ter o Python 3 e a biblioteca Flask instalados. Em seguida, execute o seguinte comando no terminal:

$ py -m flask -run

A aplicação estará disponível em "http://127.0.0.1:5000".
