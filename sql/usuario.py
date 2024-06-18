SQL_CREATE_USUARIO = '''
CREATE TABLE IF NOT EXISTS"usuario" (
	"id_usuario"	INTEGER,
	"email"	TEXT NOT NULL,
	"nome"	TEXT NOT NULL,
	"senha"	TEXT NOT NULL,
	PRIMARY KEY("id_usuario" AUTOINCREMENT)
)'''

SQL_INSERIR_USUARIO = '''
INSERT INTO usuario(email,nome,senha)
VALUES(?,?,?)
'''

SQL_ALTERAR_USUARIO = '''
UPDATE usuario
   SET email=?, nome=?, senha=?,
 WHERE id_usuario=?
'''

SQL_OBTER_TODOS_USUARIOS = '''
SELECT id_usuario, email, nome, senha
  FROM usuario
 ORDER BY email
'''

SQL_OBTER_UM_USUARIO = '''
SELECT id_usuario, email, nome, senha
  FROM usuario
 WHERE senha=?
   AND email=?
'''

SQL_EXCLUIR_USUARIO = '''
DELETE FROM usuario
 WHERE id_usuario=?
   AND email=?
'''

SQL_QUANTIDADE_USUARIOS = '''
SELECT COUNT(*) FROM usuario'''