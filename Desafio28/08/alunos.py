import sqlite3


def cadastrar_aluno():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    id_turma = input("Digite o ID da turma vinculada: ")
    
    comando_inserir = f'''
        INSERT INTO alunos(nome_aluno, idade, id_turma)
        VALUES('{nome}', {id_turma})'''

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()

def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(f"=======================\n ID: {aluno[0]}\n Nome: {aluno[1]}\n Idade: ID da escola vinculada: {turma[2]}\n=======================")#parou aqui


def atualizar_turma():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    id_turma = int(input("Digite o id da turma: "))
    novo_nome = input("Digite o novo nome da turma: ")
    novo_vinculo = int(input("Digite a nova escola vinculada: "))
    

    cursor.execute(f'''
                   UPDATE turmas
                    SET nome_turma = '{novo_nome}', id_escola = {novo_vinculo} WHERE id = {id_turma}''')
    conexao.commit()
    print("Dados atualizados com sucesso! ")
    conexao.close()


def remover_escola():
    try:
        conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")


        id_turma = int(input("Digite o ID da turma que deseja remover: "))
        cursor.execute(
            f"DELETE FROM turmas WHERE id = {id_turma}"
        )

        conexao.commit()
        
    except sqlite3.IntegrityError:
        print("A turma deve ser livre de vinculos para ser excluida.")
    finally:
        if cursor.rowcount > 0 :
            print("Turma removida com sucesso.")
        else:
            print("O ID selecionado está indísponivel para remoção ou não existe. ")
        conexao.close()