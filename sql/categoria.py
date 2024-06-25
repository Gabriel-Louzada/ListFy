SQL_CREATE_CATEGORIA = '''
CREATE TABLE IF NOT EXISTS "categoria" (
	"id_categoria"	INTEGER,
	"nome"	        TEXT NOT NULL,
	PRIMARY KEY("id_categoria" AUTOINCREMENT)
)'''

SQL_INSERIR_CATEGORIA = '''
INSERT INTO categoria(nome)
VALUES (?)
'''

SQL_ALTERAR_CATEGORIA = '''
UPDATE categoria
   SET nome=?
 WHERE id_categoria=?
'''

SQL_OBTER_TODAS_CATEGORIAS = '''
SELECT id_categoria, nome
  FROM categoria
ORDER BY nome
'''

SQL_OBTER_UM_CATEGORIA = '''
SELECT id_categoria, nome
  FROM categoria
 WHERE id_categoria=?
'''

SQL_EXCLUIR_CATEGORIA = '''
DELETE FROM categoria
 WHERE id_categoria=?
'''

SQL_QUANTIDADE_CATEGORIAS = '''
SELECT COUNT(*) FROM categoria
'''