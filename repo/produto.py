import sqlite3
from models.produto import Produto
from sql.produto import *
from util.util import criar_conexao

def criar_tabela_produto():
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CREATE_PRODUTO)
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela Produto {e}")
 
def inserir_produtos(produto: Produto):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERIR_PRODUTO,(
                produto.nome_produto,
                produto.id_categoria,
                produto.valor_produto
            ))
    except sqlite3.Error as e:
        print(f"Função inserir_produtos nao esta funcionando corretamente {e}")

def alterar_produtos(produto: Produto):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_ALTERAR_PRODUTO,(
                produto.nome_produto,
                produto.id_categoria,
                produto.valor_produto,
                produto.id_produto
            ))
    except sqlite3.Error as e:
        print(f"Função alterar_produtos nao esta funcionando corretamente {e}")

def excluir_produto(id_produto: int):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_EXCLUIR_PRODUTO, (id_produto, ))
    except sqlite3.Error as e:
        print(e)

def obter_um_produto(id_produto: int) -> Produto:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_UM_PRODUTO, (id_produto,)).fetchone()
            return Produto(*tupla)
    except sqlite3.Error as e:
        print(f"Função obter_um_produto nao esta funcionando corretamente {e}")
        return None
    
def obter_um_produto_nome(nome_produto: str) -> Produto:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            nome_produto = "%"+nome_produto+"%"
            tupla = cursor.execute(SQL_OBTER_UM_PRODUTO_NOME, (nome_produto,)).fetchone()
            return Produto(*tupla)
    except sqlite3.Error as e:
        print(f"Função obter_um_produto nao esta funcionando corretamente {e}")
        return None
    
def obter_todos_produtos() -> list[Produto]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_TODOS_PRODUTOS).fetchall()
            return [Produto(*t) for t in tupla]
    except sqlite3.Error as e:
        print(f"Função obter_todos_produtos nao esta funcionando corretamente {e}")
        return None
    
def obter_produtos_categoria(id_categoria: int) -> list[Produto]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_PRODUTOS_CATEGORIA, (id_categoria,)).fetchall()
            return [Produto(*t) for t in tupla]
    except sqlite3.Error as e:
        print(f"Função obter_um_produto_nome nao esta funcionando corretamente {e}")
        return None