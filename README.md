# Bem vindo a nossa API - Kenzie Shop 

> <font size="4" color="#fdd"> Nosso projeto tem o foco de um "Ekomerce" da Kenzie Academy com validações e verificações, reforçando a segurança e o desempenho!!! </font>


# 🥳 Rotas:
[![CUSTOMER](https://img.shields.io/badge/customer%20-%23323330.svg?&style=for-the-badge&logo=customer&logoColor=black&color=FF)](#customer)
[![ADMIN](https://img.shields.io/badge/admin%20-%23323330.svg?&style=for-the-badge&logo=cart&logoColor=black&color=AAA)](#admin)
[![AUTH](https://img.shields.io/badge/auth%20-%23323330.svg?&style=for-the-badge&logo=cart&logoColor=black&color=FDA)](#auth)
[![ADDRESS](https://img.shields.io/badge/Address%20-%23323330.svg?&style=for-the-badge&logo=customer&logoColor=black&color=FFA)](#address)
[![PRODUCTS](https://img.shields.io/badge/Products%20-%23323330.svg?&style=for-the-badge&logo=product&logoColor=black&color=D2D)](#product)
[![CART](https://img.shields.io/badge/cart%20-%23323330.svg?&style=for-the-badge&logo=cart&logoColor=black&color=AFA)](#cart)



<h1 id="customer">👤 Customer</h1>

## Requisições GET

<br>

```
Method - GET (ADMIN AUTH)

Endpoint - /customer

Body - No Content

Request - 200 
```
> <font size="4" color="#00ff2a"> Retornar todos os usuários cadastrados  </font>

<br>

```
Method - GET 

Endpoint - /customer/<customer_id>

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 200 
```
> <font size="4" color="#00ff2a"> Retornar o usuário passado pelo customer_id cadastrado </font>

<br>

## Requisições POST

```
Method - POST

Endpoint - /customer

Body - {
	"name": "Astolfo",
	"last_name": "Fagundes",
	"email": "astolfo@gmail.com",
	"password": "123456"
}

Request - 201
```
> <font size="4" color="#00ff2a"> Criação de um usuário referente ao body json passado </font>

<br>

## Requisições PATCH

```
Method - PATCH

Endpoint - /customer/<customer_id>

Header - Authorization: Bearer <token_user>

Body - {
		"name": "Rodoifo"
	}

Request - 200
```
> <font size="4" color="#00ff2a"> Alteração de informações do usuário respectivo ao customer_id podendo passar uma ou mais parametros pelo body </font>

<br>

<h1 id="admin">😎 Admin</h1>

## Requisições POST

```
Method - POST

Endpoint - /admin

Body - {
	"name": "Admin",
	"email": "admin@gmail.com",
	"password": "123456"
}

Request - 201
```
> <font size="4" color="#00ff2a"> Criação do Admin </font>


<br>

<h1 id="auth">👾 Auth</h1>

## Requisições POST

```
Method - POST

Endpoint - /auth/admin

Body - {
	"email": "admin@gmail.com",
	"password": "123456"
}

Request - 200
```
> <font size="4" color="#00ff2a"> Validação de admin, retornando o token </font>

</br>

```
Method - POST

Endpoint - /auth/customer

Body - {
	"email": "customer@gmail.com",
	"password": "123456"
}

Request - 200
```
> <font size="4" color="#00ff2a"> Validação de usuário, retornando o token </font>

</br>

<h1 id="address">🗺 Address</h1>

## Requisições GET

<br>

```
Method - GET 

Endpoint - /customer/<customer_id>/address

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 200 
```
> <font size="4" color="#00ff2a"> Retornar apenas os endereços do usuário respectivo  </font>

<br>

```
Method - GET 

Endpoint - /address/<address_id>

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 200 
```
> <font size="4" color="#00ff2a"> Retornar apenas um endereço especifico  </font>

<br>

## Requisições POST
```
Method - POST

Endpoint - /customer/<customer_id>/address

Header - Authorization: Bearer <token_user>

Body - {
		"name": "Rua Dom Pedro II",
		"number": 79,
		"complement": "Casa", 
		"zipcode": "12345-678", 		
		"city": "João Pessoa",		
		"state": "PB"		
	}

Request - 201
```

> <font size="4" color="#00ff2a"> Creação do endereço relacionando ao usuário respectivo </font>

<br>

## Requisições PATCH
```
Method - PATCH

Endpoint - /address/<address_id>

Header - Authorization: Bearer <token_user>

Body - {
		"name": "Rua Fragoso perreira frantz"	
	}

Request - 200
```
> <font size="4" color="#00ff2a"> Alteração de informações do endereço respectivo ao address_id podendo passar uma ou mais parametros pelo body</font>

<br>
<h1 id="product">📦  Products</h1>

## Requisições GET
```
Method - GET 

Endpoint - /product

Body - No Content

Request - 200 
```
> <font size="4" color="#00ff2a"> Retornar todos os produtos cadastrados </font>

<br>

```
Method - GET 

Endpoint - /product/<product_id>

Body - No Content

Request - 200 
```
> <font size="4" color="#00ff2a"> Retornar o produto especifico passado pelo product_id </font>

<br>
 
## Requisições POST (ADMIN)
```
Method - POST (ADMIN)

Endpoint - /product

Header - Authorization: Bearer <token_admin>

Body - {
	"name":"Camiseta",
	"description":"Camiseta Branca M",
	"current_price":29.99,
	"discount":0,
	"amount_products":100,
	"image_url":"https://img.elo7.com.br/product/main/2256D07/camiseta-branca-malha-fria-camiseta-para-trabalho.jpg"
}

Request - 201
```
> <font size="4" color="#00ff2a"> Alteração de informações do endereço respectivo ao address_id podendo passar uma ou mais parametros pelo body</font>

<br>

## Requisições PATCH (ADMIN) 
```
Method - PATCH (ADMIN)

Endpoint - /product/<product_id>

Header - Authorization: Bearer <token_admin>

Body - {
	"description":"Camiseta Preta G",
	"current_price":55

}

Request - 201
```
> <font size="4" color="#00ff2a"> Alteração de informações do produto respectivo ao product_id podendo passar uma ou mais parametros pelo body</font>

</br>

## Requisições DELETE (ADMIN) 
```
Method - DELETE (ADMIN)

Endpoint - /product/<product_id>

Header - Authorization: Bearer <token_admin>

Body - No Content

Request - 200
```
> <font size="4" color="#00ff2a">Deletando produto referente ao product_id</font>

</br>

<h1 id="cart">🛒 Cart</h1>

## Requisições GET
```
Method - GET 

Endpoint - /customers/<customer_id>/cart/

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 200 
```
> <font size="4" color="#00ff2a"> Retornar todos os produtos do carrinho referente ao usuário </font>

</br>

## Requisições POST

```
Method - POST

Endpoint - /customers/<customer_id>/cart/<product_id>

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 201
```
> <font size="4" color="#00ff2a"> Adicionar um produto ao carrinho do usuário referente ao customer_id e o produto referente ao product_id  </font>



