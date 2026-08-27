import sqlite3
conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def cadastrar_rede():
    conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    nome = input("Digite o nome da rede: ")
    cnpj = int(input("Digite o CNPJ da rede: "))
    
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS redes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cnpj INTEGER NOT NULL
                )''')


    comando_inserir = f'''
        INSERT INTO redes(nome, cnpj)
        VALUES('{nome}', {cnpj})'''

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()


def listar_redes():
    conexao.commit()
    cursor.execute("SELECT * FROM redes")
    redes = cursor.fetchall()
    for rede in redes:
        print(f"=======================\n ID: {rede[0]}\n nome: {rede[1]}\n cnpj: {rede[2]}\n=======================")


def atualizar_rede():
    conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    id_rede = int(input("Digite o id da rede: "))
    novo_nome = input("Digite o novo nome da rede: ")
    novo_cnpj = int(input("Digite o novo cnpj: "))


def remover_rede():
    try:
        conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")


        id_rede = int(input("Digite o ID da rede que deseja remover: "))
        cursor.execute(
            f"DELETE FROM redes WHERE id = {id_rede}"
        )

        conexao.commit()
        
    except sqlite3.IntegrityError:
        print("A rede deve ser livre de vinculos para ser excluida.")
    finally:
        if cursor.rowcount > 0 :
            print("Rede removida com sucesso.")
        else:
            print("O ID selecionado está indísponivel para remoção ou não existe. ")
        conexao.close()


def menu_redes():
    try:
        
        opcao = 0
        while opcao != 5:
            print("==================================\n 1 - CADASTRAR REDE\n 2 - LISTAR REDES\n 3 - ATUALIZAR REDES\n 4 - REMOVER REDES\n 5 - SAIR\n==================================")
            opcao = int(input("Digite sua ação: "))
            if opcao == 1:
                cadastrar_rede()
            elif opcao == 2:
                listar_redes()
            elif opcao == 3:
                atualizar_rede()
            elif opcao == 4:
                remover_rede()
            elif opcao == 5:
                break
            elif opcao not in (1, 2, 3, 4, 5):
                print("Insira uma opção válida")
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    finally:
        if opcao != 5:
            print("Tente novamente")
            menu_redes()
        elif opcao == 5:
            print("Fechando menu das redes")
        else:
            menu_redes()