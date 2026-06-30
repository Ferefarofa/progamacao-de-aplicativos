import sqlite3

def inicializar_banco():
    conexao = sqlite.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL
        )
    ''')
    #O banco não está salvando as alterações por quê ?
    
    conexao.commit()
    conexao.close()

    #Não está salvando pois o código não possui o comando "conexao.commit()" após criação da tabela.