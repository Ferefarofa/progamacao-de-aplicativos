import sqlite3
conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def cadastrar_turma():
    erro = False
    try:
        conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        nome = input("Digite o nome da turma: ")
        id_escola = int(input("Digite o ID da escola vinculada: "))

        assert nome != "", "O nome não deve ser nulo."
        assert id_escola > 0, "O ID de vinculo deve ser maior que zero."

        comando_inserir = f'''
            INSERT INTO turmas(nome_turma, id_escola)
            VALUES('{nome}', {id_escola})'''

        cursor.execute(comando_inserir)
        conexao.commit()
        assert cursor.rowcount == 1, "O cadastro não foi feito."


    except sqlite3.IntegrityError:
        erro = True
        print("O ID de vinculo não existe.")

    except AssertionError as ala:
        erro = True
        print("Erro de cadastro, ", ala)

    finally:
        if erro:

            print("Tente novamente")
        else:
            
            print("Cadastro feito com sucesso.")
        conexao.close()

def listar_turmas():
    cursor.execute("SELECT * FROM turmas")
    turmas = cursor.fetchall()
    for turma in turmas:
        print(f"=======================\n ID: {turma[0]}\n Nome: {turma[1]}\n ID da escola vinculada: {turma[2]}\n=======================")


def atualizar_turma():
    erro = False
    try:
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
        assert cursor.rowcount == 1, "A atualização falhou, verifique se o ID inserido existe."
    except AssertionError or sqlite3Error:
        erro = True
        print("A atualização falhou, verifique se o ID inserido existe.")
    finally:
        if erro:
            print("Tente novamente.")
        else:
            print("Dados atualizados com sucesso! ")
        conexao.close()


def remover_turma():
    erro = False
    try:
        conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")


        id_turma = int(input("Digite o ID da turma que deseja remover: "))

        assert id_turma > 0, "O ID deve ser válido."
        cursor.execute(
            f"DELETE FROM turmas WHERE id = {id_turma}"
        )

        conexao.commit()
        assert cursor.rowcount == 1, "A turma com o ID inserido não existe."
    except AssertionError as ala:

        erro = True
        print("Erro de remoção, ", ala)

    finally:
        if erro:

            print("Tente novamente.")
        else:

            print("Turma removida com sucesso.")
        conexao.close()