import sqlite3
from models.lista import Lista
from sql.lista import *
from util import criar_conexao

def criar_tabela_lista():
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CREATE_LISTA)
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela lista {e}")

def obter_todos_lista() -> list[Lista]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_TODOS_LISTA).fetchall()
            return [Lista(*t) for t in tupla]
    except sqlite3.Error as e:
        print(f"Função obter_todos_lista nao esta funcionando corretamente {e}")
        return None 
    
def inserir_lista(lista: Lista):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERIR_LISTA,(
                lista.estabelecimento,
                lista.id_user,
                lista.status_lista
            ))
    except sqlite3.Error as e:
        print(e)

def alterar_LISTA(lista: Lista):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_ALTERAR_LISTA,(
                lista.estabelecimento,
                lista.id_user,
                lista.status_lista
            ))
    except sqlite3.Error as e:
        print(e)

def excluir_lista(id_lista: int):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_EXCLUIR_LISTA, (id_lista, ))
    except sqlite3.Error as e:
        print(e)

def obter_uma_lista(id_lista: int) -> Lista:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_UM_LISTA, (id_lista,)).fetchone()
            return Lista(*tupla)
    except sqlite3.Error as e:
        print(f"Função obter_uma_lista nao esta funcionando corretamente {e}")
        return None