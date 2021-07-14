# Bem vindo a nossa API - Kenzie Shop 

> Nosso projeto tem o foco de um "Ekomerce" da Kenzie Academy com validações e verificações, reforçando a segurança e o desempenho!!!


# 🥳 Rotas:

# ⚖ Customer
## Requisições GET
```
Method - GET 

Endpoint - /customer

Body - No Content

Request - 200 
```
> Retornar todos os usuários cadastrados  

```
Method - GET 

Endpoint - /customer/customer_id

Body - No Content

Request - 200 
```
> Retornar o usuário passado pelo customer_id cadastrado

```
Method - GET 

Endpoint - /customer/customer_id

Body - No Content

Request - 200 
```
> Retornar o usuário passado pelo customer_id cadastrado

## Requisições POST

```
Method - POST

Endpoint - /customer

Body - {
	"name": "Testinho",
	"last_name": "Testonio",
	"email": "teste@teste.com",
	"password": "123456"
}

Request - 201
```
> Criação de um usuário teste referente ao body json passado

## Requisições PATCH

```
Method - PATCH

Endpoint - /customer/customer_id

Body - {
	"name": "testorinoldo"
}

Request - 200
```
> Alteração de informações do usuário respectivo ao customer_id podendo passar uma ou mais parametros pelo body



