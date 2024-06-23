SQL_CREATE_PROMOCAO = """
CREATE TABLE IF NOT EXISTS "promocao" (
	"id_produto"	    INTEGER,
	"valor_promocao"	REAL NOT NULL,
	"id_lista"	      INTEGER,
    PRIMARY KEY("id_produto","id_lista"),
	FOREIGN KEY("id_produto") REFERENCES "produto"("id_produto"),
    FOREIGN KEY("id_lista") REFERENCES "lista"("id_lista")
	
);
"""

SQL_INSERT_PROMOCAO = """
INSERT INTO promocao(id_produto,valor_promocao,id_lista)
       VALUES(?,?,?)
"""

SQL_ALTERAR_PROMOCAO = """
UPDATE promocao
   SET id_produto=?, valor_promocao=?, estabelecimento=?
 WHERE id_promocao=?
"""

SQL_EXCLUIR_PROMOCAO = """
DELETE FROM promocao
 WHERE id_promocao=?
   AND id_produto=?
"""

# PRIMEIRO ESBOÇO de certa forma subo a informação da lista toda do cliente para criar uma promocao
SQL_CRIAR_PROMOCAO = """
SELECT itens_lista.id_produto,
       itens_lista.valor,
	     itens_lista.id_lista
  FROM itens_lista
 where itens_lista.id_lista = ?
"""

SQL_OBTER_TODAS_PROMOCOES = """
SELECT promocao.id_produto,
       min(promocao.valor_promocao),
	     lista.id_lista,
	     lista.estabelecimento,
       produto.nome_produto  
  from promocao,
       produto,
	   lista
 where promocao.id_lista = lista.id_lista
   and promocao.id_produto = produto.id_produto
 group by promocao.id_produto
"""

SQL_QUANTIDADE_PROMOCAO = """
SELECT COUNT(*) FROM promocao
"""
