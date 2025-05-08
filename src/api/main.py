import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sqlite3 import Error
from flask import Flask, jsonify, request
from database.criar_banco import conectar_banco

app = Flask(__name__)

@app.route("/produtos", methods=["GET"])
def produtos():
    try:
        conectar = conectar_banco()
        cursor = conectar.cursor()
        
        cursor.execute("SELECT * FROM produtos")
        dados = cursor.fetchall()
        
        produtos = []
        
        for produto in dados:
            produtos.append(
                {
                    "id": produto[0],
                    "cdbarras": produto[1],
                    "nome": produto[2],
                    "quantidade": produto[3],
                    "preco": produto[4]
                }
            )
        return jsonify(produtos)
    except Error as e:
        return jsonify({"erro": f"Ocorreu um erro ao listar os produtos: {e}"}), 400
    finally:
        conectar.close()

@app.route("/produtos", methods=["POST"])
def cadastrar_produto():
    try:
        dados = request.get_json()
        
        campos_obrigatorios = ["cdbarras", "nome", "quantidade", "preco"]
        
        for campo in campos_obrigatorios:
            if campo not in dados:
                return jsonify({"erro": f"Campo obrigatório '{campo}' não informado."}), 400
        
        conectar = conectar_banco()
        cursor = conectar.cursor()
        
        cursor.execute(
            """ 
            INSERT INTO produtos (cdbarras, nome, quantidade, preco) VALUES (?, ?, ?, ?)
            """,
            (
                dados["cdbarras"],
                dados["nome"],
                dados["quantidade"],
                dados["preco"]
            )
        )
        
        conectar.commit()
        return jsonify({"mensagem": "Produto cadastrado com sucesso!"}), 201
    except Error as e:
        return jsonify({"erro": f"Erro ao cadastrar produto: {e}"}), 500
    finally:
        conectar.close()

@app.route("/produtos/<int:id>", methods=["PUT"])
def atualizar_produto(id):
    try:
        dados = request.get_json()
        
        conectar = conectar_banco()
        cursor = conectar.cursor()
        
        campos = ["cdbarras", "nome", "quantidade", "preco"]
        campos_validos = [campo for campo in campos if campo in dados]
        
        if not campos_validos:
            return jsonify({"erro": "Nenhum dado válido enviado para atualização."}), 400
        
        query = f"UPDATE produtos SET {",".join([f'{campo} = ?' for campo in campos_validos])} WHERE id = ?"
        valores = [dados[campo] for campo in campos_validos]
        valores.append(id)
        
        cursor.execute(query, valores)
        conectar.commit()

        return jsonify({"mensagem": "Produto atualizado com sucesso!"}), 200
    except Error as e:
        return jsonify({"erro": f"Ocorreu um erro ao atualizar: {e}"}), 400
    finally:
        conectar.close()

@app.route("/produtos/<int:id>", methods=["DELETE"])
def apagar_produto(id):
    try:
        conectar = conectar_banco()
        cursor = conectar.cursor()
        
        cursor.execute("DELETE FROM produtos WHERE id = ?",(id,))
        conectar.commit()
        
        if cursor.rowcount == 0:
            return jsonify({"mensagem": "Produto não encontrado."}), 404
        
        return jsonify({"mensagem": "Produto apagado com sucesso!"}), 200
    except Error as e:
        return jsonify({"erro": f"Ocorreu um erro ao apagar produto: {e}"}), 500
    finally:
        conectar.close()
        
@app.route("/produtos/<int:id>", methods=["GET"])
def buscar_produto(id):
    try:
        conectar = conectar_banco()
        cursor = conectar.cursor()
        
        cursor.execute("SELECT * FROM produtos WHERE id = ?",(id,))
        dados = cursor.fetchone()
        
        if dados is None:
            return jsonify({"mensagem": "Produto não encontrado."}), 404
        
        produto = {
            "id": dados[0],
            "cdbarras": dados[1],
            "nome": dados[2],
            "quantidade": dados[3],
            "preco": dados[4]
        }
        
        return jsonify(produto), 200
    except Error as e:
        return jsonify({"erro": f"Ocorreu um erro ao buscar o produto: {e}"}), 500
    finally:
        conectar.close()
    

if __name__ == "__main__":
    from database.criar_banco import criar_banco
    criar_banco()
    app.run(debug=True)