import sqlite3
import os

def conectar_banco():
    caminho_database = os.path.abspath(os.path.join(os.path.dirname(__file__), "produtos.db"))
    return sqlite3.connect(caminho_database)

def criar_banco():
    
    conectar = conectar_banco()
    cursor = conectar.cursor()
    
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cdbarras TEXT NOT NULL,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
        """
    )
    
    conectar.commit()
    conectar.close()

if __name__ == "__main__":
    criar_banco()