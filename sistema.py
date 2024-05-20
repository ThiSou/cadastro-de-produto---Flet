import mysql
import mysql.connector

class Gerenciador:
    def __init__(self):
        self.conect = mysql.connector.connect(
            host="",
            user="",
            password="",
            database=""
        )
        self.cursor = self.conect.cursor()

    def testar_conexao(self):
        return self.conect.is_connected()
    
    def criar_tabela_estoque(self):
        self.cursor.execute("""  CREATE TABLE IF NOT EXISTS estoque_produtos (
                    nome_produto TEXT,
                    quantidade_produto TEXT,
                    preço_produto TEXT,
                    marca_produto TEXT); """)
        
        self.conect.commit()
        
    def cadastrar_produto(self,nome,quantidade,preco,marca):
        self.cursor.execute(""" INSERT INTO  estoque_produtos (nome_produto,quantidade_produto,preço_produto,marca_produto)
                            VALUES (%s,%s,%s,%s);""", (nome,quantidade,preco,marca))
        self.conect.commit()

    def buscar_produto(self,nome):
        self.cursor.execute(""" SELECT * FROM estoque_produtos WHERE nome_produto = %s""",(nome,))
        produtos = self.cursor.fetchone()
        return produtos
    

gerenciador = Gerenciador()


