SQL_CREATE_PROMOCAO = '''
CREATE TABLE IF NOT EXISTS "promocao" (
	"id_promocao"	INTEGER,
	"id_produto"	INTEGER NOT NULL,
	"valor_promocao"	REAL NOT NULL,
	"estabelecimento"	TEXT NOT NULL,
	PRIMARY KEY("id_promocao" AUTOINCREMENT),
	FOREIGN KEY("id_produto") REFERENCES produto(id_produto), 
	FOREIGN KEY("estabelecimento") REFERENCES lista(id_lista)
)
'''

SQL_INSERT_PROMOCAO = '''
INSERT INTO promocao(id_produto,valor_promocao,estabelecimento)
       VALUES(?,?,?)
'''

SQL_ALTERAR_PROMOCAO = '''
UPDATE promocao
   SET id_produto=?, valor_promocao=?, estabelecimento=?
 WHERE id_promocao=?
'''

SQL_OBTER_TODOS_PROMOCAO = '''
SELECT id_promocao, id_produto, valor_promocao, estabelecimento
  FROM promocao
'''

SQL_OBTER_UMA_PROMOCAO = '''
SELECT id_promocao, id_produto, valor_promocao, estabelecimento
  FROM promocao
 WHERE id_produto=?
'''

SQL_EXCLUIR_PROMOCAO = '''
DELETE FROM promocao
 WHERE id_promocao=?
   AND id_produto=?
'''

SQL_QUANTIDADE_PROMOCAO = '''
SELECT COUNT(*) FROM promocao
'''