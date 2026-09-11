import sqlite3
conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def cadastrar_aluno():
    erro = False
    try:
        conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        id_turma = int(input("Digite o ID da turma vinculada: "))
        
        assert nome != "", "O nome não deve ser nulo."
        assert idade > 0, "Idade inválida."
        assert id_turma > 0, "O ID de vinculo deve ser maior que zero."

        comando_inserir = f'''
            INSERT INTO alunos(nome_aluno, idade, id_turma)
            VALUES('{nome}', {idade}, {id_turma})'''

        cursor.execute(comando_inserir)
        conexao.commit()
        assert cursor.rowcount == 1,"O cadastro falhou."


    except sqlite3.IntegrityError:
        print("O ID de vinculo não existe.")
        erro = True
    
    except AssertionError as ala:
        print("Erro de cadastro, ", ala)

    finally:
        if erro:

            print("Tente novamente.")
        else:

            print("Cadastro feito com sucesso.")
        conexao.close()

def listar_alunos():
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    for aluno in alunos:
        print(f"=======================\n ID: {aluno[0]}\n Nome: {aluno[1]}\n Idade: {aluno[2]}\n ID da turma vinculada: {aluno[3]}\n=======================")


def atualizar_aluno():
    erro = False
    try:
        conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        id_aluno = int(input("Digite o id do aluno: "))
        novo_nome = input("Digite o novo nome do aluno: ")
        nova_idade = int(input("Digite a nova idade do aluno: "))
        novo_vinculo = int(input("Digite o ID da nova turma vinculada: "))
        
        assert novo_nome != "", "O nome não deve ser nulo."
        assert nova_idade > 0, "Idade inválida."

        cursor.execute(f'''
                    UPDATE alunos
                        SET nome_aluno = '{novo_nome}', idade = {nova_idade}, id_turma = {novo_vinculo} WHERE id = {id_aluno}''')
        conexao.commit()
        assert cursor.rowcount == 1, "A atualização falhou."
    except sqlite3.IntegrityError:
        erro = True
        print("O ID de vinculo não existe.")

    except AssertionError as ala:
        erro = True
        print("Erro de atualização, ", ala)

    finally:
        if erro:

            print("Tente novamente.")
        else:

            print("Dados atualizados com sucesso! ")
        conexao.close()


def remover_aluno():
    erro = False
    try:
        conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")


        id_aluno = int(input("Digite o ID do aluno que deseja remover: "))
        assert id_aluno > 0, "O ID deve ser válido."
        cursor.execute(
            f"DELETE FROM alunos WHERE id = {id_aluno}"
        )

        conexao.commit()
        assert cursor.rowcount == 1, "O aluno com o ID inserido não existe."
    except AssertionError as ala:

        erro = True
        print("Erro de remoção, ", ala)
    finally:
        if erro:

            print("Tente novamente.")
        else:

            print("Aluno removido com sucesso.")
        conexao.close()