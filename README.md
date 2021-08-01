# Kenzie Pet 🐶
O Kenzie Pet é um sistema desenvolvido para PetShops, com o objetivo de automatizar a tarefa de guardar dados dos animais que são atendidos em PetShops.

Ao utilizar esta API, deve ser possível criar informações de animais, bem como listar ou excluir tais informações.

## Como instalar e rodar? 🚀
Para instalar o sistema, é necessário seguir alguns passos, como baixar o projeto e fazer instalação das dependências. Para isso, é necessário abrir uma aba do terminal e digitar o seguinte:

## Este passo é para baixar o projeto
git clone https://gitlab.com/ximitti/kenzie-pet.git
Depois que terminar de baixar, é necessário entrar na pasta, criar um ambiente virtual e entrar nele:

## Entrar na pasta
	cd kenzie_pet

## Criar um ambiente virtual

    python3 -m venv venv

	# Entrar no ambiente virtual:
	source venv/bin/activate

	# Então, para instalar as dependências, basta:
    pip install -r requirements.txt

	# Depois de ter instalado as dependências, é necessário rodar as migrations para que o banco de dados e as tabelas sejam criadas:
	./manage.py migrate
    
	# Então, para rodar, basta digitar o seguinte, no terminal:
	./manage.py runserver
E o sistema estará rodando em http://127.0.0.1:8000/

## Utilização 🖥️
Para utilizar este sistema, é necessário utilizar um API Client, como o Insomnia

**Rotas**
**GET /api/animals/**

Esta rota retorna todos os animais cadastrados no banco.

	RESPONSE STATUS -> HTTP 200 (ok)

Response:

	[
	  {
	    "id": 1,
	    "name": "Bidu",
	    "age": 1.0,
	    "weight": 30.0,
	    "sex": "macho",
	    "group": {
	      "id": 1,
	      "name": "cao",
	      "scientific_name": "canis familiaris"
	    },
	    "characteristic_set": [
	      {
	        "id": 1,
	        "characteristic": "peludo"
	      },
	      {
	        "id": 2,
	        "characteristic": "medio porte"
	      }
	    ]
	  },
	  {
	    "id": 2,
	    "name": "Hanna",
	    "age": 1.0,
	    "weight": 20.0,
	    "sex": "femea",
	    "group": {
	      "id": 2,
	      "name": "gato",
	      "scientific_name": "felis catus"
	    },
	    "characteristic_set": [
	      {
	        "id": 1,
	        "characteristic": "peludo"
	      },
	      {
	        "id": 3,
	        "characteristic": "felino"
	      }
	    ]
	  }
	]

**GET /api/animals/<**int:animal_id**>/**
Esta rota retorna as informações do animal com id igual ao passado na rota.

	RESPONSE STATUS -> HTTP 200 (ok)

Response:

	{
	  "id": 1,
	  "name": "Bidu",
	  "age": 1.0,
	  "weight": 30.0,
	  "sex": "macho",
	  "group": {
	    "id": 1,
	    "name": "cao",
	    "scientific_name": "canis familiaris"
	  },
	  "characteristic_set": [
	    {
	      "id": 1,
	      "characteristic": "peludo"
	    },
	    {
	      "id": 2,
	      "characteristic": "medio porte"
	    }
	  ]
	}
    
**POST /api/animals/**
Esta rota é para a criação de informações de animais.

	RESPONSE STATUS -> HTTP 201 (created)
    
Body:

	{
	  "name": "Bidu",
	  "age": 1,
	  "weight": 30,
	  "sex": "macho",
	  "group": {
	    "name": "cao",
	    "scientific_name": "canis familiaris"
	  },
	  "characteristic_set": [
	    {
	      "characteristic": "peludo"
	    },
	    {
	      "characteristic": "medio porte"
	    }
	  ]
	}
    
Response:

	{
	  "id": 1,
	  "name": "Bidu",
	  "age": 1.0,
	  "weight": 30.0,
	  "sex": "macho",
	  "group": {
	    "id": 1,
	    "name": "cao",
	    "scientific_name": "canis familiaris"
	  },
	  "characteristic_set": [
	    {
	      "id": 1,
	      "characteristic": "peludo"
	    },
	    {
	      "id": 2,
	      "characteristic": "medio porte"
	    }
	  ]
	}
    
**DELETE /api/animals/<**int:animal_id**>/**
Rota para deletar as informações de um animal.

Não há conteúdo no retorno da requisição.

	RESPONSE STATUS -> HTTP 204 (no content)
    
## Tecnologias utilizadas 📱
* Django
* Django Rest Framework
* SQLite
___________________________________________
### Licence
MIT
