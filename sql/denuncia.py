SQL_CREATE_DENUNCIA = '''
CREATE TABLE IF NOT EXISTS "denuncia" (
	"id_denuncia"	INTEGER,
	"id_usuario"	INTEGER,
	"assunto"	    TEXT NOT NULL,
	"descricao"	    TEXT NOT NULL,
  "data"          TEXT NOT NULL,
	CONSTRAINT "pk_denuncia" PRIMARY KEY("id_denuncia" AUTOINCREMENT),
	CONSTRAINT "fk_denuncia_usuario" FOREIGN KEY("id_usuario") REFERENCES "usuario"("id_usuario")
);
'''
SQL_INSERIR_DENUNCIA = '''
INSERT INTO denuncia(id_usuario, assunto, descricao,data)
VALUES(?,?,?,CURRENT_DATE)
'''
SQL_ALTERAR_DENUNCIA = '''
UPDATE denuncia
   SET assunto=?, descricao=?
 WHERE id_denuncia=?
   AND id_usuario=?
'''

SQL_OBTER_TODAS_DENUNCIAS = '''
SELECT id_denuncia, id_usuario, assunto, descricao, strftime("%d-%m-%Y", data) AS data_formatada
  FROM denuncia
 order by data
'''

SQL_OBTER_DENUNCIA_ID = '''
SELECT id_denuncia, id_usuario, assunto, descricao, strftime("%d-%m-%Y", data) AS data_formatada
  FROM denuncia
 WHERE id_denuncia=?
'''

SQL_OBTER_DENUNCIA_USUARIO = '''
SELECT id_denuncia, id_usuario, assunto, descricao
  FROM denuncia
 WHERE id_usuario=?
 order by assunto
'''

SQL_REMOVER_DENUNCIA = '''
DELETE FROM denuncia
 WHERE id_denuncia=?
   AND id_usuario=?
'''