import sqlite3

conexao = sqlite3.connect('escola.demonstracao.db')
cursor = conexao.cursor()


cursor.execute('''ALTER TABLE alunos ADD COLUMN
               estado TEXT''')