import sqlite3
from typing import Optional
from models.usuario import Usuario
from sql.usuario import *
from util.util import criar_conexao

def criar_tabela_usuario():
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_CREATE_USUARIO)
    except sqlite3.Error as e:
        print(e)

def obter_todos_usuarios() -> list[Usuario]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_TODOS_USUARIOS).fetchall()
            return [Usuario(*t) for t in tupla]
    except sqlite3.Error as e:
        print(f"Função obter_todos_usuarios nao esta funcionando corretamente {e}")
        return None 

def alterar_token(id_usuario: int, token: str):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_ALTERAR_TOKEN, (token, id_usuario))
    except sqlite3.DatabaseError as e:
        print(e)

def inserir_usuario(usuario: Usuario) -> Optional[Usuario]:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERIR_USUARIO,(
                usuario.email,
                usuario.nome,
                usuario.senha
            ))
            if cursor.rowcount > 0:
                usuario.id_usuario = cursor.lastrowid
                return usuario
    except sqlite3.Error as e:
        print(e)
        return None

def alterar_usuario(usuario: Usuario):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_ALTERAR_USUARIO,(
                usuario.email,
                usuario.nome,
                usuario.id_usuario
            ))
    except sqlite3.Error as e:
        print(e)

def excluir_usuario(id_usuario: int):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_EXCLUIR_USUARIO, (id_usuario, ))
    except sqlite3.Error as e:
        print(e)

def obter_um_usuario(id:int) -> Usuario:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_POR_ID, (id,)).fetchone()
            return Usuario(*tupla)
    except sqlite3.Error as e:
        print(f"Função obter_um_usuario nao esta funcionando corretamente {e}")
        return None
    
def obter_por_email(email:str) -> Usuario:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_POR_EMAIL, (email,)).fetchone()
            return Usuario(*tupla)
    except sqlite3.Error as e:
        print(f"Função obter_por_email nao esta funcionando corretamente {e}")
        return None

def obter_por_token(token:str) -> Usuario:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_POR_TOKEN, (token,)).fetchone()
            return Usuario(*tupla)
    except sqlite3.Error as e:
        print(f"Função obter_por_token nao esta funcionando corretamente {e}")
        return None

def obter_usuario_logado():
    pass