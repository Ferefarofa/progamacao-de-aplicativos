import sqlite3    

def coisar():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO alunos (nome, turma) VALUES (?, ?)",(nome_aluno, turma_aluno))
    conexao.commit()


nome_aluno = input("Digite o nome do aluno: ")
turma_aluno = int(input("Digite a Turma do aluno: "))
coisar()