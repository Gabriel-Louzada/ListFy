import sqlite3
from models.itens_lista import Itens_lista
from sql.itens_lista import *
from util import criar_conexao

def criar_tabela_itens_lista():
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CREATE_ITENS_LISTA)
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela Itens_Lista {e}")

def obter_todas_itens_lista() -> list[Itens_lista]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_TODOS_ITENS_LISTA).fetchall()
            return [Itens_lista(*t) for t in tuplas]
    except sqlite3.Error as e:
        print(f"Função obter_todas_itens_lista não esta funcionando corretamente {e}")
        return None 
    
def obter_todas_itens_lista_nome() -> list[Itens_lista]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_TODOS_ITENS_LISTA).fetchall()
            return [Itens_lista(*t) for t in tuplas]
    except sqlite3.Error as e:
        print(f"Função obter_todas_itens_lista não esta funcionando corretamente {e}")
        return None 


def obter_itens_lista_nomes(id_lista:int) -> list[Itens_lista]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_ITENS_LISTA_NOMES,(id_lista,)).fetchall()
            return [Itens_lista(*t) for t in tuplas]
    except sqlite3.Error as e:
        print(f"Função obter_todas_itens_lista não esta funcionando corretamente {e}")
        return None 

def inserir_itens_lista(itens_lista: Itens_lista):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERT_ITENS_LISTA,(
                itens_lista.id_produto,
                itens_lista.id_lista,
                itens_lista.quantidade,
                itens_lista.valor_produto
            ))
    except sqlite3.Error as e:
        print(f"Função inserir_itens_lista não esta funcionando corretamente {e}")

def alterar_itens_lista(itens_lista: Itens_lista):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_ALTERAR_ITENS_LISTA,(
                itens_lista.quantidade,
                itens_lista.valor_produto,
                itens_lista.id_produto,
                itens_lista.id_lista ))
    except sqlite3.Error as e:
        print(f"Função alterar_itens_lista não esta funcionando corretamente {e}")

def excluir_itens_lista(id_lista: int,id_produto: int):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_EXCLUIR_ITENS_LISTA, (id_lista,id_produto))
    except sqlite3.Error as e:
        print(f"Função excluir_itens_lista não esta funcionando corretamente {e}")

def obter_item_lista(id_produto: int) -> Itens_lista:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_UM_ITENS_LISTA, (id_produto,)).fetchone()
            return Itens_lista(*tupla)
    except sqlite3.Error as e:
        print(f"Função alterar_itens_lista não esta funcionando corretamente {e}")
        return None