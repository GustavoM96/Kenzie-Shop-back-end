# Bem vindo a nossa API - Kenzie Shop 

> <font size="4" color="#fdd"> Nosso projeto tem o foco de um "Ekomerce" da Kenzie Academy com validações e verificações, reforçando a segurança e o desempenho!!! </font>


# 🥳 Rotas:
[![Validando](https://img.shields.io/badge/Validando%20-%23323330.svg?&style=for-the-badge&logo=Criando&logoColor=black&color=dDF)](#validando)
[![Criando](https://img.shields.io/badge/Criando%20-%23323330.svg?&style=for-the-badge&logo=Criando&logoColor=black&color=FF)](#criando)
[![Buscando](https://img.shields.io/badge/Buscando%20-%23323330.svg?&style=for-the-badge&logo=Buscando&logoColor=black&color=AAA)](#buscando)
[![Alterando](https://img.shields.io/badge/Alterando%20-%23323330.svg?&style=for-the-badge&logo=Alterando&logoColor=black&color=FDA)](#alterando)
[![Deletando](https://img.shields.io/badge/Deletando%20-%23323330.svg?&style=for-the-badge&logo=customer&logoColor=black&color=FFA)](#deletando)

# 👾 Validando Acessos

<h2 id="validando" style="font-size:20px; color:#cdd; font-weight:bold">Para ter acesso a maior parte dos componentes precisamos validar a entrada</h2>

<p style="font-size:18px; color:#00ff2a; font-weight:bold">Validação do admin</p>

```
Method - POST

Endpoint - /auth/admins

Body - {
	"email": "admin@gmail.com",
	"password": "123456"
}

Request - 200
```
> <p style="font-size:16px;color:#00ff2a"> Retornando o token de acesso do admin </p>

</br>
<img src="https://i.ibb.co/0K7QFFf/Auth-Admin.png" alt="01" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>

</br>

<p style="font-size:18px; color:#00ff2a; font-weight:bold">Validação do usuário</p>

```
Method - POST

Endpoint - /auth/customers

Body - {
	"email": "customer@gmail.com",
	"password": "123456"
}

Request - 200
```
> <p style="font-size:16px;color:#00ff2a"> Retornando o token de acesso do usuário </p>

</br>

<img src="https://i.ibb.co/VQ0sqt5/AuthUser.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>

</br>

# 👤 Criando Elementos

<h2 style="font-size:20px; color:#cdd; font-weight:bold; text-align:center">Aqui está todas as informações que você poderá inserir na API</h2>

</br>

<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Criando um admin</p>

```
Method - POST

Endpoint - /admins

Body - {
	"name": "Admin",
	"email": "admin@gmail.com",
	"password": "123456"
}

Request - 201
```
> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorna admin referente as informações passada por body</p>

</br>

<img src="https://i.ibb.co/bF06wJM/03.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Criando um usuário</p>

```
Method - POST

Endpoint - /customers

Body - {
	"name": "Silvio",
	"last_name": "Romano",
	"email": "Silvio@gmail.com",
	"password": "123456"
}

Request - 201
```
> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorna usuário referente as informações passada por body</p>

</br>

<img src="https://i.ibb.co/VYrLjNy/04.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>

<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Adicionando Endereço ao usuário</p>

```
Method - POST

Endpoint - /customers/<int:customer_id>/addresses

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
> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorna endereço referente ao body</p>

<img src="https://i.ibb.co/NjHtm5V/05.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>


</br>


<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Adicionando um produto ao sistema (Apenas Admin)</p>

```
Method - POST (ADMIN)

Endpoint - /products

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
> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorna produto referente ao body</p>

<img src="https://i.ibb.co/ZxzG2K2/06.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>


<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Adicionar produto ao carinho do usuário</p>

```
Method - POST

Endpoint - /customers/<int:customer_id>/cart/products/<int:product_id>

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 201
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorno do produto adicionado</p>

<img src="https://i.ibb.co/8YMsRsG/07.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>



<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Criando Ordem ao comprar item</p>

```
Method - POST

Endpoint - /customers/<int:customer_id>/orders

Header - Authorization: Bearer <token_user>

Body - {
	"invoice_url": https://url_tested_matrix;
	"payment_type": Cartão de Credito;
}

Request - 201
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorno a ordem da compra</p>

<img src="https://i.ibb.co/ZgX0D4J/Address-Order.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>


<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Enviando Email da compra</p>

```
Method - POST

Endpoint - /customers/<int:customer_id>/addresses/<int:address_id>/orders/<int:order_id>/email

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 201
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Envia Email para o usuário da compra</p>

<img src="https://i.ibb.co/TtQvKK5/email.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>

</br>

# 👾 Pegando elementos da API


<h2 style="font-size:20px; color:#cdd; font-weight:bold; text-align:center">Aqui estão todos os elementos que podem ser buscados na API</h2>


<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Trazendo todos os usuários cadastrados (APENAS ADMINs)</p>


```
Method - GET (ADMIN)

Endpoint - /customers

Body - No Content

Request - 200 
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorna todos os usuários cadastrados</p>

<img src="https://i.ibb.co/rkT4wmh/09.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>


<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Trazendo usuário respectivo</p>

```
Method - GET 

Endpoint - /customers/<int:customer_id>

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 200 
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorna um usuário respectivo</p>

<img src="https://i.ibb.co/PTMTsM7/10.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>

<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Trazendo todos os endereços de um usuário </p>


```
Method - GET 

Endpoint - /customers/<int:customer_id>/addresses

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 200 
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorna todos os endereços cadastrados de um usuário</p>

<img src="https://i.ibb.co/S7p3mGv/11.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>

<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Trazendo endereços especificos dos usuários </p>

```
Method - GET 

Endpoint - /customers/<int:customer_id>/addresses/<int:address_id>

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 200 
```


> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorno</p>

<img src="https://i.ibb.co/xCvRvyK/adresss.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>


<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Trazendo todos os endereços (APENAS ADMINs) </p>




```
Method - GET (ADMIN)

Endpoint - /addresses

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 200 
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorno</p>

<img src="https://i.ibb.co/L54JKyD/12.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

</br>


<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Trazendo endereço especifico (APENAS ADMINs) </p>


```
Method - GET (ADMIN)

Endpoint - /addresses/<int:address_id>

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 200 
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Retorno</p>

<img src="https://i.ibb.co/g77bQKm/13.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>


# 👾 Modificando Elementos da API


<h2 style="font-size:20px; color:#cdd; font-weight:bold; text-align:center">Aqui estão todos os elementos que podem ser Modificados na API</h2>


</br>


<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Fazendo alterações no usuário </p>


```
Method - PATCH

Endpoint - /customers/<int:customer_id>

Header - Authorization: Bearer <token_user>

Body - {
		"name": "Romano",
		"last_name": "Silvio",
		"email":"Romano@gmail.com",
	}

Request - 200
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Devem passar pelo menos um item no body, quantidade opcional</p>

<img src="https://i.ibb.co/VVGms5s/14.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>


</br>

<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Fazendo alterações no endereço</p>


```
Method - PATCH

Endpoint - /customers/<int:customer_id>/addresses/<int:address_id>

Header - Authorization: Bearer <token_user>

Body - {
		"name": "Rua Dom Torreto",
		"number": 857,
		"complement": "Apartamento", 
		"zipcode": "12345-698", 		
		"city": "Curitiba",		
		"state": "PR"		
	}

Request - 200
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Devem passar pelo menos um item no body, quantidade opcional</p>

<img src="https://i.ibb.co/Xz19pSB/15.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>


</br>

<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Fazendo alterações no produto (APENAS ADMINs)</p>

```
Method - PATCH (ADMIN)

Endpoint - /products/<int:product_id>

Header - Authorization: Bearer <token_admin>

Body - {
	"name":"Camiseta G",
	"description":"Camiseta Laranja",
	"current_price":44.99,
	"discount":22,
	"amount_products":110,
	"image_url":"https://img.elo7.com.br/product/main/2256D07/camiseta-branca-malha-fria-camiseta-para-trabalho.jpg"
}

Request - 201
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Devem passar pelo menos um item no body, quantidade opcional</p>

<img src="https://i.ibb.co/5v3jzSK/16.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>


</br>

<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Fazendo alterações na quantidade de um produto no cart</p>

```
Method - PATCH 

Endpoint - /customers/<int:customer_id>/cart/products/<int:product_id>?quantity_product=value

Header - Authorization: Bearer <token_user>

Body - No Content

Request - 201
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Valor passado por url quantity_product</p>

<img src="https://i.ibb.co/PYVWwkt/17.png" style="width:300%; border:solid 1px green, margin:0 auto;"/>



<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Fazendo alteração no order</p>

```
Method - PATCH 

Endpoint - /customers/<int:customer_id>/orders/<int:order_id>

Header - Authorization: Bearer <token_user>

Body - {
	"payment_type": "Boleto",
	"invoice_url": "https://fiscal_boletod"
}

Request - 201
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Devem passar pelo menos um item no body, quantidade opcional</p>

<img src="https://i.ibb.co/s9V2LYN/orders.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>

# 👾 Deletando elementos da API


<h2 style="font-size:20px; color:#cdd; font-weight:bold; text-align:center">Aqui estão todos os elementos que podem ser deletados da API</h2>

</br>

<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Deletando todos os produtos do carrinho de um usuário </p>


```
Method - DELETE

Endpoint - /customers/<int:customer_id>/cart

Header - Authorization: Bearer <token_user>

Body - no content

Request - 204
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Sem Retorno</p>

<img src="https://i.ibb.co/rsmdyhG/delete-all-cart.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>


<p style="font-size:18px; color:#00ff2a; font-weight:bold; text-align:center">Deletando Produto especifico do carrinho de um usuário </p>


```
Method - DELETE

Endpoint - /customers/<int:customer_id>/cart/products/<int:product_id>

Header - Authorization: Bearer <token_user>

Body - no content

Request - 204
```

> <p style="font-size:16px;color:#00ff2a; text-align:center">Sem Retorno</p>

<img src="https://i.ibb.co/Xb6qBVL/Delete-cart-one.png" style="width:100%; border:solid 1px green, margin:0 auto;"/>
