SQL_CREATE_USUARIO = '''
CREATE TABLE IF NOT EXISTS "usuario" (
	"id_usuario"	INTEGER,
	"email"	TEXT NOT NULL UNIQUE,
	"nome"	TEXT NOT NULL,
	"senha"	TEXT NOT NULL,
	"token"	TEXT,
	PRIMARY KEY("id_usuario" AUTOINCREMENT)
);'''

SQL_INSERIR_USUARIO = '''
INSERT INTO usuario(email,nome,senha)
VALUES(?,?,?)
'''

SQL_ALTERAR_TOKEN = """
    UPDATE usuario
    SET token=?
    WHERE id_usuario=?
"""

SQL_ALTERAR_USUARIO = '''
UPDATE usuario
   SET email=?, nome=?, senha=?,
 WHERE id_usuario=?
'''
SQL_ALTERAR_SENHA = '''
    UPDATE usuario
    SET senha=?
    WHERE id=?
'''

SQL_OBTER_TODOS_USUARIOS = '''
SELECT id_usuario, email, nome, senha
  FROM usuario
 ORDER BY email
'''

SQL_OBTER_POR_ID = '''
SELECT id_usuario, email, nome, senha
  FROM usuario
 WHERE id_usuario=?
'''

SQL_OBTER_POR_EMAIL= '''
  SELECT id_usuario, email, nome, senha, token
  FROM usuario
  WHERE email=? 
'''
SQL_OBTER_POR_TOKEN= '''
  SELECT id_usuario, email, nome, senha, token
  FROM usuario
  WHERE token=?
'''

SQL_EXCLUIR_USUARIO = '''
DELETE FROM usuario
 WHERE id_usuario=?
'''

SQL_QUANTIDADE_USUARIOS = '''
SELECT COUNT(*) FROM usuario'''