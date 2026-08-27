import sqlite3
conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")


def cadastrar_loja():
    conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    nome = input("Digite o nome da loja: ")
    endereco = input("Digite o endereco da loja: ")
    id_rede = int(input("Digite o id da rede vinculado a loja: "))
    
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS lojas(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                endereco TEXT NOT NULL,
                id_rede INTEGER NOT NULL,
                FOREIGN KEY (id_rede) REFERENCES redes(id)
                )''')

                
    comando_inserir = f'''
        INSERT INTO lojas(nome, endereco, id_rede)
        VALUES('{nome}', '{endereco}', {id_rede})'''

    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()


def listar_lojas():
    conexao.commit()
    cursor.execute("SELECT * FROM lojas")
    lojas = cursor.fetchall()
    for loja in lojas:
        print(f"=======================\n ID: {loja[0]}\n nome: {loja[1]}\n endereço: {loja[2]}\n ID/Rede vinculada: {loja[3]}\n=======================")


def atualizar_loja():
    conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    id_loja = int(input("Digite o id da loja: "))
    novo_nome = input("Digite o novo nome da loja: ")
    novo_endereco = input("Digite o novo endereco da loja: ")
    novo_id_rede = int(input("Digite a nova rede vinculada: "))


def remover_loja():
    conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    
    id_loja = int(input("Digite o ID da loja que deseja remover: "))
    cursor.execute(
        f"DELETE FROM lojas WHERE id = {id_loja}"
    )

    conexao.commit()
    if cursor.rowcount > 0 :
        print("Loja removida com sucesso.")
    else:
        print("Nenhuma loja encontrada com esse ID. ")
    conexao.close()


def menu_lojas():
    try:
        
        opcao = 0
        while opcao != 5:
            print("==================================\n 1 - CADASTRAR LOJA\n 2 - LISTAR LOJAS\n 3 - ATUALIZAR LOJAS\n 4 - REMOVER LOJAS\n 5 - SAIR\n==================================")
            opcao = int(input("Digite sua ação: "))
            if opcao == 1:
                cadastrar_loja()
            elif opcao == 2:
                listar_lojas()
            elif opcao == 3:
                atualizar_loja()
            elif opcao == 4:
                remover_loja()
            elif opcao == 5:
                break
            elif opcao not in (1, 2, 3, 4, 5):
                print("Insira uma opção válida")
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    except sqlite3.IntegrityError:
        print("ID de vínculo não existe")
    finally:
        if opcao != 5:
            print("Tente novamente")
            menu_lojas()
        elif opcao == 5:
            print("Fechando menu das lojas")
        else:
            menu_lojas()