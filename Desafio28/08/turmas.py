import sqlite3


def cadastrar_turma():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    nome = input("Digite o nome da turma: ")
    id_escola = input("Digite o ID da escola vinculada: ")
    
    comando_inserir = f'''
        INSERT INTO turmas(nome_turma, id_escola)
        VALUES('{nome}', {id_escola})'''

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()

def listar_turmas():
    cursor.execute("SELECT * FROM turmas")
    turmas = cursor.fetchall()
    for turma in turmas:
        print(f"=======================\n ID: {turma[0]}\n Nome: {turma[1]}\n ID da escola vinculada: {turma[2]}\n=======================")


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