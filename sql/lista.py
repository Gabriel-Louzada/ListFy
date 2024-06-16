SQL_CREATE_LISTA = '''
CREATE TABLE IF NOT EXISTS "lista" (
	"id_lista"	            INTEGER,
	"estabelecimento"	      TEXT    NOT NULL,
	"id_user"	              INTEGER NOT NULL,
  "status_lista"     		  INTEGER NOT NULL,
	FOREIGN KEY("id_user") REFERENCES "usuario"("id_user"),
	PRIMARY KEY("id_lista" AUTOINCREMENT)
)'''

SQL_INSERIR_LISTA = '''
INSERT INTO lista(estabelecimento, id_user, status_lista)
VALUES(?,?,?)
'''

#NESSE UPDATE ESTOU ATRIBUINDO QUE NAO FAZ SENTIDO ALTERAR O ID DO USUARIO DE DENTRO DA LISTA 
SQL_ALTERAR_LISTA = '''
UPDATE lista
   SET estabelecimento=?, status_lista=?
 WHERE id_lista=?
'''

SQL_FECHAR_LISTA = '''
UPDATE lista
   SET status_lista=0
 WHERE id_lista=?
'''

SQL_OBTER_TODOS_LISTA = '''
SELECT id_lista, estabelecimento,id_user, status_lista 
  FROM lista
 ORDER BY estabelecimento
'''

SQL_OBTER_UM_LISTA = '''
SELECT id_lista, estabelecimento,id_user, status_lista 
  FROM lista
 WHERE id_lista=?
'''

#Nao irei permitir a exclusao de uma lista que ja esta fechada
#status = 1
SQL_EXCLUIR_LISTA = '''
DELETE FROM lista
 WHERE id_lista=?
   AND status_lista = 1
'''

SQL_QUANTIDADE_LISTAS = """
    SELECT COUNT(*) FROM lista
"""
SQL_DROP_LISTA = '''
DROP TABLE lista
'''