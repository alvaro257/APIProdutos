import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sqlite3 import Error
from flask import Flask, jsonify
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



if __name__ == "__main__":
    from database.criar_banco import criar_banco
    criar_banco()
    app.run(debug=True)