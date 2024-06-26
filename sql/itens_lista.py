SQL_CREATE_ITENS_LISTA = '''
CREATE TABLE IF NOT EXISTS "itens_lista" (
	"id_itens_lista"	INTEGER,
	"id_produto"	    INTEGER NOT NULL,
	"id_lista"	      INTEGER NOT NULL,
	"quantidade"	    REAL NOT NULL,
	"valor"	          REAL NOT NULL,
	FOREIGN KEY("id_produto") REFERENCES "produto"("id_produto"),
	FOREIGN KEY("id_lista") REFERENCES "lista"("id_lista"),
	PRIMARY KEY("id_itens_lista" AUTOINCREMENT))'''

SQL_OBTER_ITENS_LISTA_NOMES = """
SELECT itens_lista.id_produto,
       itens_lista.id_lista,
       itens_lista.quantidade,
       itens_lista.valor,
	     produto.nome_produto
  FROM itens_lista,
	   produto
 WHERE itens_lista.id_produto = produto.id_produto
   AND itens_lista.id_lista = ?
"""

SQL_INSERT_ITENS_LISTA = '''
INSERT INTO itens_lista(id_produto, id_lista, quantidade, valor)
VALUES (?,?,?,?)
'''

#MEU USUARIO NAO TERA A PERMISSAO DE TIRAR UM PRODUTO DE UMA LISTA E ACRESCENTAR EM OUTRA COM. POR ISSO O ID_LISTA NAO ESTA NO SET
SQL_ALTERAR_ITENS_LISTA = '''
UPDATE itens_lista
   SET quantidade=?, valor=?
 WHERE id_produto=?
   AND id_lista=?
'''

SQL_OBTER_TODOS_ITENS_LISTA = '''
SELECT id_produto, id_lista, quantidade, valor
  FROM itens_lista
ORDER BY id_produto
'''

SQL_OBTER_TODOS_ITENS_LISTA_NOME = '''
SELECT id_produto, id_lista, quantidade, valor
  FROM itens_lista
ORDER BY id_produto
'''

SQL_OBTER_UM_ITEM_LISTA = '''
SELECT id_produto, id_lista, quantidade, valor
  FROM itens_lista
 WHERE id_lista=?
'''

SQL_EXCLUIR_ITENS_LISTA = '''
DELETE FROM itens_lista
 WHERE id_lista=?
   AND id_produto=?
'''

SQL_QUANTIDADE_ITENS_LISTA = """
    SELECT COUNT(*) FROM itens_lista
"""