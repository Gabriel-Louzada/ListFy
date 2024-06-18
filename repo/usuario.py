import sqlite3
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

def inserir_usuario(usuario: Usuario):
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            cursor.execute(SQL_INSERIR_USUARIO,(
                usuario.email,
                usuario.nome,
                usuario.senha
            ))
    except sqlite3.Error as e:
        print(e)

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

def obter_um_usuario(senha: str, email:str) -> Usuario:
    try:
        with criar_conexao() as conexao:
            cursor = conexao.cursor()
            tupla = cursor.execute(SQL_OBTER_UM_USUARIO, (senha,email)).fetchone()
            return Usuario(*tupla)
    except sqlite3.Error as e:
        print(f"Função obter_um_usuario nao esta funcionando corretamente {e}")
        return None
    
def obter_usuario_logado():
    pass