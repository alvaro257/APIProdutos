# API de Produtos (Flask + SQLite)

Este projeto é uma API simples construída com **Flask** e **SQLite** para gerenciar produtos.  
Ela permite cadastrar, listar, atualizar, buscar e apagar produtos armazenados no banco.

---

## Como rodar o projeto

### Pré-requisitos

- Python 3.x
- Virtualenv (opcional, mas recomendado)

---

### Passos para instalação

Clone este repositório:

```bash
git clone https://github.com/alvaro257/APIProdutos.git
```

(Opcional) Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Inicie a aplicação:

```bash
python app.py
```

O servidor estará acessível em:
```
http://127.0.0.1:5000
```

---

## Endpoints disponíveis

### Listar todos os produtos

```
GET /produtos
```

### Buscar um produto por ID

```
GET /produtos/<id>
```

### Cadastrar um novo produto

```
POST /produtos
```

Exemplo de JSON no body:

```json
{
  "cdbarras": "123456789",
  "nome": "Produto Exemplo",
  "quantidade": 10,
  "preco": 19.99
}
```

### Atualizar um produto existente

```
PUT /produtos/<id>
```

Exemplo de JSON no body:

```json
{
  "nome": "Novo Nome",
  "preco": 29.99
}
```

### Apagar um produto

```
DELETE /produtos/<id>
```

---

## Testando a API com Postman (ou ferramenta similar)

Você pode testar os endpoints da API utilizando o Postman ou qualquer ferramenta semelhante de envio de requisições HTTP.

### Exemplos de requisições:

1. **Listar todos os produtos**  
   Método: `GET`  
   URL: `http://127.0.0.1:5000/produtos`

2. **Buscar um produto por ID**  
   Método: `GET`  
   URL: `http://127.0.0.1:5000/produtos/<id>`

3. **Cadastrar um novo produto**  
   Método: `POST`  
   URL: `http://127.0.0.1:5000/produtos`  
   Corpo da requisição (JSON):

   ```json
   {
     "cdbarras": "123456789",
     "nome": "Produto Exemplo",
     "quantidade": 10,
     "preco": 19.99
   }
   ```

4. **Atualizar um produto existente**  
   Método: `PUT`  
   URL: `http://127.0.0.1:5000/produtos/<id>`  
   Corpo da requisição (JSON):

   ```json
   {
     "nome": "Novo Nome",
     "preco": 29.99
   }
   ```

5. **Apagar um produto**  
   Método: `DELETE`  
   URL: `http://127.0.0.1:5000/produtos/<id>`