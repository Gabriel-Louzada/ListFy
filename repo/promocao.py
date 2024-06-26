import sqlite3
from models.promocao import Promocao
from sql.promocao import *
from util.util import criar_conexao

def criar_tabela_promocao():
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CREATE_PROMOCAO)
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela promocao {e}")

def obter_todas_promocoes() -> list[Promocao]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_TODAS_PROMOCOES).fetchall()
            return [Promocao(*t) for t in tuplas]
    except sqlite3.Error as e:
        print(f"Função obter_todas_promocao não esta funcionando corretamente {e}")
        return None 
    
def inserir_promocao(promocao: Promocao):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERT_PROMOCAO,(
                promocao.id_produto,
                promocao.valor_promocao,
                promocao.id_lista
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

def criar_promocao(id_lista: int):
    try:
         with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_CRIAR_PROMOCAO,(id_lista,)).fetchall()
            if tuplas:
                promocao = [Promocao(*t) for t in tuplas]
                for p in promocao:
                    inserir_promocao(p)
            else:
                print("erro na função criar_promocao")
    except sqlite3.Error as e:
        print(f"Função criar_promocao nao esta Funcionando corretamente {e}")
