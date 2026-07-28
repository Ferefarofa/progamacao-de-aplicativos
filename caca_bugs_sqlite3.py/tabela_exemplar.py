import sqlite3
conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def cadastrar_aluno():


    cursor.execute('''
                CREATE TABLE IF NOT EXISTS turmas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_turma TEXT NOT NULL,
                FOREIGN KEY (id_serie) REFERENCES series(id),
                FOREIGN KEY (id_professor) REFERENCES professores(id)
                )''')


cadastrar_aluno()
    
conexao.commit()

