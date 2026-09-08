import sqlite3


def cadastrar_escola():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    nome = input("Digite o nome da escola: ")
    cidade = input("Digite a cidade localizada: ")
    
    comando_inserir = f'''
        INSERT INTO escolas(nome, cidade)
        VALUES('{nome}', {cidade})'''

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()

def listar_escolas():
    cursor.execute("SELECT * FROM escolas")
    escolas = cursor.fetchall()
    for escola in escolas:
        print(f"=======================\n ID: {escola[0]}\n Nome: {escola[1]}\n Cidade: {escola[2]}\n=======================")


def atualizar_escola():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    id_escola = int(input("Digite o id da escola: "))
    novo_nome = input("Digite o novo nome da escola: ")
    novo_municipio = int(input("Digite o novo município: "))
    

    cursor.execute(f'''
                   UPDATE escolas
                    SET nome = '{novo_nome}', cidade = {novo_municipio} WHERE id = {id_escola}''')
    conexao.commit()
    print("Dados atualizados com sucesso! ")
    conexao.close()


def remover_escola():
    try:
        conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")


        id_escola = int(input("Digite o ID da escola que deseja remover: "))
        cursor.execute(
            f"DELETE FROM escolas WHERE id = {id_escola}"
        )

        conexao.commit()
        
    except sqlite3.IntegrityError:
        print("A escola deve ser livre de vinculos para ser excluida.")
    finally:
        if cursor.rowcount > 0 :
            print("Rede removida com sucesso.")
        else:
            print("O ID selecionado está indísponivel para remoção ou não existe. ")
        conexao.close()