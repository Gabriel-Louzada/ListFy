import sqlite3
from models.promocao import Promocao
from sql.promocao import *
from util import criar_conexao

def criar_tabela_promocao():
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CREATE_PROMOCAO)
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela promocao {e}")

def obter_todas_promocao() -> list[Promocao]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_TODOS_PROMOCAO).fetchall()
            return [Promocao(*t) for t in tuplas]
    except sqlite3.Error as e:
        print(f"Função obter_todas_promocao não esta funcionando corretamente {e}")
        return None 
    
def inserir_promocao(promocao: Promocao):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERT_PROMOCAO,(
                promocao.id_promocao,
                promocao.id_produto,
                promocao.valor_promocao,
                promocao.estabelecimento
            ))
    except sqlite3.Error as e:
        print(f"Função inserir_promocao não esta funcionando corretamente {e}")

def alterar_promocao(promocao: Promocao):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_ALTERAR_PROMOCAO,(promocao.id_promocao,
                promocao.id_produto,
                promocao.valor_promocao,
                promocao.estabelecimento ))
    except sqlite3.Error as e:
        print(f"Função alterar_promocao não esta funcionando corretamente {e}")

def excluir_promocao(id_promocao: int):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_EXCLUIR_PROMOCAO, (id_promocao, ))
    except sqlite3.Error as e:
        print(f"Função excluir_promocao não esta funcionando corretamente {e}")

def obter_uma_promocao(id_promocao: int) -> Promocao:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_UMA_PROMOCAO, (id_promocao,)).fetchone()
            return Promocao(*tupla)
    except sqlite3.Error as e:
        print(f"Função alterar_promocao não esta funcionando corretamente {e}")
        return None