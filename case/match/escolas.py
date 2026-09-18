import sqlite3
conexao = sqlite3.connect('case/match/gestao_escolar.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

def cadastrar_escola():
    erro = False
    try:
        conexao = sqlite3.connect('case/match/gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        nome = input("Digite o nome da escola: ")
        cidade = input("Digite a cidade localizada: ")
        
        comando_inserir = f'''
            INSERT INTO escolas(nome, cidade)
            VALUES('{nome}', '{cidade}')'''

        assert nome != "", "O nome não pode ser nulo."
        assert cidade != "", "A cidade não pode ser nula."

        cursor.execute(comando_inserir)
        conexao.commit()
        assert cursor.rowcount == 1, "A escola não foi cadastrada"
    
    except AssertionError as ala:
        erro = True
        print("Erro de cadastro, ", ala) 

    finally:
        if erro:

            print("Tente novamente")
        else:

            print("Cadastro feito com sucesso.")

        conexao.close()

def listar_escolas():
    cursor.execute("SELECT * FROM escolas")
    escolas = cursor.fetchall()
    assert escolas != "", "Nenhuma escola cadastrada."
    for escola in escolas:
        print(f"=======================\n ID: {escola[0]}\n Nome: {escola[1]}\n Cidade: {escola[2]}\n=======================")


def atualizar_escola():
    erro = False
    try:
        conexao = sqlite3.connect('case/match/gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        id_escola = int(input("Digite o id da escola: "))
        novo_nome = input("Digite o novo nome da escola: ")
        novo_municipio = input("Digite o novo município: ")
        assert novo_nome != "", "O nome não deve ser nulo."
        assert novo_municipio != "", "O município não deve ser nulo."

        cursor.execute(f'''
                    UPDATE escolas
                        SET nome = '{novo_nome}', cidade = '{novo_municipio}' WHERE id = {id_escola}''')
        conexao.commit()
        assert cursor.rowcount == 1, "A atualização de dados falhou."

    except AssertionError as ala:
        erro = True
        print("Erro de atualização, ", ala)

    finally:
        if erro:

            print("Tente novamente.")
        else:

            print("Dados atualizados com sucesso! ")
        conexao.close()

def remover_escola():
    erro = False
    try:
        conexao = sqlite3.connect('case/match/gestao_escolar.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")

        id_escola = int(input("Digite o ID da escola que deseja remover: "))
        assert id_escola > 0, "O ID deve ser válido."

        cursor.execute(
            f"DELETE FROM escolas WHERE id = {id_escola}"
        )

        conexao.commit()
        assert cursor.rowcount == 1, "A escola com o ID inserido não existe."
    
    except AssertionError as ala:
        erro = True
        print("Erro de remoção, ", ala)

    finally:
        if erro:

            print("Tente novamente.")
        else:

            print("Escola removida com sucesso.")
        conexao.close()