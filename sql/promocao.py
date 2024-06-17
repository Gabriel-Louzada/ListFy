SQL_CREATE_PROMOCAO = '''
CREATE TABLE IF NOT EXISTS "promocao" (
	"id_promocao"	INTEGER,
	"id_produto"	INTEGER NOT NULL,
	"valor_promocao"	REAL NOT NULL,
	"estabelecimento"	TEXT NOT NULL,
    "nome_produto"	    TEXT NOT NULL,
	PRIMARY KEY("id_promocao" AUTOINCREMENT),
	FOREIGN KEY("id_produto") REFERENCES produto(id_produto), 
	FOREIGN KEY("estabelecimento") REFERENCES lista(id_lista)
)
'''

SQL_INSERT_PROMOCAO = '''
INSERT INTO promocao(id_produto,valor_promocao,estabelecimento,nome_produto)
       VALUES(?,?,?,?)
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

#PRIMEIRO ESBOÇO
SQL_CRIAR_PROMOCAO = '''
SELECT itens_lista.id_produto,
       min(itens_lista.valor) AS VALOR_PROMOCAO,
	   lista.estabelecimento,
	   produto.nome_produto
  FROM itens_lista,
       lista,
	   produto
 WHERE itens_lista.id_lista = lista.id_lista
   AND produto.id_produto = itens_lista.id_produto
GROUP BY itens_lista.id_produto, lista.estabelecimento,produto.nome_produto
'''

SQL_QUANTIDADE_PROMOCAO = '''
SELECT COUNT(*) FROM promocao
'''