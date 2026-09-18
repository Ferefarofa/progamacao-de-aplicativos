import sqlite3
conexao = sqlite3.connect('case/match/gestao_escolar.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def criar_tabela_escolas():
    conexao = sqlite3.connect('case/match/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS escolas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cidade TEXT NOT NULL
                )''')

    conexao.commit()
    conexao.close()


def criar_tabela_turmas():
    conexao = sqlite3.connect('case/match/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_turma TEXT NOT NULL,
                id_escola INTEGER,
                FOREIGN KEY (id_escola) REFERENCES escolas(id) ON DELETE CASCADE
                )''')

    conexao.commit()
    conexao.close()


def criar_tabela_alunos():
    conexao = sqlite3.connect('case/match/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
                CREATE TABLE IF NOT EXISTS alunos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_aluno TEXT NOT NULL,
                idade INTEGER NOT NULL,
                id_turma INTEGER,
                FOREIGN KEY (id_turma) REFERENCES turmas(id) ON DELETE CASCADE
                )''')

    conexao.commit()
    conexao.close()

def hello_gestao_escolar():
    criar_tabela_escolas()
    criar_tabela_turmas()
    criar_tabela_alunos()