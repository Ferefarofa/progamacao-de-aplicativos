import sqlite3
conexao = sqlite3.connect('escola.demosntracao.db')
cursor = conexao.cursor()


nome_completo_aluno = input("Digite o nome completo: ")
telefone_aluno = input("Digite o telefone: ")
turma_aluno = input("Digite a Turma: ")
idade_aluno = int(input("Digite a idade: "))
cpf_aluno = input("Digite o cpf: ")

cursor.execute('''
               CREATE TABLE IF NOT EXISTS alunos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               nome TEXT NOT NULL,
               telefone TEXT, 
               turma TEXT, 
               idade INTEGER,
               cpf TEXT UNIQUE NOT NULL)''')
comando_inserir = f'''
    INSERT INTO alunos(nome, telefone, turma, idade, cpf)
    VALUES('{nome_completo_aluno}', '{telefone_aluno}', '{turma_aluno}', '{idade_aluno}', '{cpf_aluno}')'''

cursor.execute(comando_inserir)
conexao.commit()

conexao.commit()
cursor.execute("SELECT * FROM alunos")
for linha in cursor.fetchall():
    print(linha)

conexao.close()