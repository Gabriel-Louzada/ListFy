import sqlite3
from models.categoria import Categoria
from sql.categoria import *
from util.util import criar_conexao

def criar_tabela_categoria():
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CREATE_CATEGORIA)
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela Categoria {e}")


def obter_todas_categorias() -> list[Categoria]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_TODAS_CATEGORIAS).fetchall()
            return [Categoria(*t) for t in tuplas]
    except sqlite3.Error as e:
        print(f"Função obter_todas_categorias não esta funcionando corretamente {e}")
        return None 
    
def inserir_categoria(categoria: Categoria):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERIR_CATEGORIA,(categoria.nome_categoria, ))
    except sqlite3.Error as e:
        print(f"Função inserir_categoria não esta funcionando corretamente {e}")

def alterar_categoria(categoria: Categoria):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERIR_CATEGORIA,(categoria.nome_categoria, ))
    except sqlite3.Error as e:
        print(f"Função alterar_categoria não esta funcionando corretamente {e}")

def excluir_categoria(id_categoria: int):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_EXCLUIR_CATEGORIA, (id_categoria, ))
    except sqlite3.Error as e:
        print(f"Função excluir_categoria não esta funcionando corretamente {e}")

def obter_uma_categoria(id_categoria: int) -> Categoria:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_UM_CATEGORIA, (id_categoria,)).fetchone()
            return Categoria(*tupla)
    except sqlite3.Error as e:
        print(f"Função alterar_categoria não esta funcionando corretamente {e}")
        return None