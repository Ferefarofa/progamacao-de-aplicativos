import sqlite3
conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def cadastrar_tabela():


    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tumra INTEGER NOT NULL

                )''')


cadastrar_tabela
    
conexao.commit()

