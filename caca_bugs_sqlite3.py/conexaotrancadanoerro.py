import sqlite3
def cadastrar_turma(nome, id_serie, id_prof):
conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = oN:")
# se o id_prof não existir, ocorre um Integrityerror.
# Se o erro acontecer, o que ocorre com a linha conexao.close()>
cursor.execute("INSERT INTO turmas (nome turma, id_serie, id_professor) VALUES (?,?,P)",(nome,id_serie, id_prof))
conexao.commit()
conexao.close()