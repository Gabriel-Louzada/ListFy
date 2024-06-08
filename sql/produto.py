SQL_CREATE_PRODUTO = '''
CREATE TABLE IF NOT EXISTS "produto" (
	"id_produto"	INTEGER,
	"nome_produto"	TEXT NOT NULL,
	"id_categoria"	INTEGER NOT NULL,
	"valor_produto"	REAL NOT NULL,
	PRIMARY KEY("id_produto" AUTOINCREMENT),
	FOREIGN KEY("id_categoria") REFERENCES "categoria"("id_categoria")
)'''

SQL_INSERIR_PRODUTO ='''
INSERT INTO produto(nome_produto, id_categoria, valor_produto)
VALUES (?,?,?)
'''

SQL_ALTERAR_PRODUTO = '''
UPDATE produto
   SET nome_produto=?, id_categoria=?, valor_produto=?
 WHERE id_produto=?
'''

SQL_OBTER_TODOS_PRODUTOS = '''
SELECT id_produto, nome_produto, id_categoria, valor_produto
  FROM produto
ORDER BY nome_produto
'''

SQL_OBTER_UM_PRODUTO ='''
SELECT id_produto, nome_produto, id_categoria, valor_produto
  FROM produto
 WHERE id_produto=?
'''
SQL_EXCLUIR_PRODUTO = '''
DELETE FROM produto
 WHERE id_produto=?
'''
SQL_QUANTIDADE_PRODUTOS = '''
SELECT COUNT(*) FROM produto
'''

SQL_OBTER_UM_PRODUTO_NOME ='''
SELECT id_produto, nome_produto, id_categoria, valor_produto
  FROM produto
 WHERE nome_produto LIKE ?
'''
SQL_OBTER_PRODUTOS_CATEGORIA ='''
SELECT id_produto, nome_produto, id_categoria, valor_produto
  FROM produto
 WHERE id_categoria = ?
'''