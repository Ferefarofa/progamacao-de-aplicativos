import sqlite3


def criar_tabela_escolas():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS escolas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade CIDADE NOT NULL
                )''')

    conexao.commit()
    conexao.close()


def criar_tabela_turmas():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_turma TEXT NOT NULL,
                id_escola INTEGER NOT NULL,
                FOREIGN KEY (id_escola) FROM escolas(id) ON DELETE CASCADE
                )''')

    conexao.commit()
    conexao.close()


def criar_tabela_alunos():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_aluno TEXT NOT NULL,
                idade INTEGER NOT NULL,
                id_turma INTEGER NOT NULL,
                FOREIGN KEY (id_turma) FROM turmas(id) ON DELETE CASCADE
                )''')

    conexao.commit()
    conexao.close()