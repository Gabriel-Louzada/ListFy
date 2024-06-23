import sqlite3
from models.denuncia import Denuncia
from sql.denuncia import *
from util.util import criar_conexao

def criar_tabela_denuncia():
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CREATE_DENUNCIA)
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela Denuncia {e}")

def obter_todas_denuncias() -> list[Denuncia]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_TODAS_DENUNCIAS).fetchall()
            return [Denuncia(*t) for t in tuplas]           
    except sqlite3.Error as e:
        print(f"Erro na funcao obter_todas_denuncias {e}")

def obter_todas_denuncias_por_usuario() -> list[Denuncia]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tuplas = cursor.execute(SQL_OBTER_DENUNCIA_USUARIO).fetchall()
            return [Denuncia(*t) for t in tuplas]           
    except sqlite3.Error as e:
        print(f"Erro na funcao obter_todas_denuncias {e}")

def obter_denuncia_por_id(id_denuncia:int) -> Denuncia:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_DENUNCIA_ID, (id_denuncia,)).fetchone()
            return Denuncia(*tupla)         
    except sqlite3.Error as e:
        print(f"Erro na funcao obter_todas_denuncias_por_id {e}")


def alterar_denuncia(denuncia: Denuncia):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_ALTERAR_DENUNCIA,(
                denuncia.id_usuario,
                denuncia.assunto,
                denuncia.descricao
            ))          
    except sqlite3.Error as e:
        print(f"Erro na funcao inserir_denuncia {e}")

def inserir_denuncia(denuncia: Denuncia):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERIR_DENUNCIA,(
                denuncia.id_usuario,
                denuncia.assunto,
                denuncia.descricao
            ))
            if cursor.rowcount > 0:
                denuncia.id_denuncia = cursor.lastrowid
    except sqlite3.Error as e:
        print(f"Erro na funcao inserir_denuncia {e}")

def excluir_denuncia(id_denuncia: int, id_usuario:int):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_REMOVER_DENUNCIA,(id_denuncia, id_usuario))
            if cursor.rowcount > 0:
                return print("Denuncia Removida com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro na funcao excluir_denuncia {e}")
    