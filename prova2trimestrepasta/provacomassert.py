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

    assert nome != ""
    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()

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


    assert nome != ""
    assert endereco != ""
    cursor.execute(comando_inserir)
    conexao.commit()
    conexao.close()
    
def listar_redes():
    conexao.commit()
    cursor.execute("SELECT * FROM redes")
    redes = cursor.fetchall()
    assert redes != ""
    for rede in redes:
        print(f"=======================\n ID: {rede[0]}\n nome: {rede[1]}\n cnpj: {rede[2]}\n=======================")

def listar_lojas():
    conexao.commit()
    cursor.execute("SELECT * FROM lojas")
    lojas = cursor.fetchall()
    for loja in lojas:
        print(f"=======================\n ID: {loja[0]}\n nome: {loja[1]}\n endereço: {loja[2]}\n ID/Rede vinculada: {loja[3]}\n=======================")

def atualizar_rede():
    conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    id_rede = int(input("Digite o id da rede: "))
    novo_nome = input("Digite o novo nome da rede: ")
    novo_cnpj = int(input("Digite o novo cnpj: "))
    

    cursor.execute(f'''
                   UPDATE redes
                    SET nome = '{novo_nome}', cnpj = {novo_cnpj} WHERE id = {id_rede}''')
    conexao.commit()
    print("Dados atualizados com sucesso! ")
    conexao.close()

def atualizar_loja():
    conexao = sqlite3.connect('prova2trimestrepasta/banco_mercado.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    id_loja = int(input("Digite o id da loja: "))
    novo_nome = input("Digite o novo nome da loja: ")
    novo_endereco = input("Digite o novo endereco da loja: ")
    novo_id_rede = int(input("Digite a nova rede vinculada: "))
    

    cursor.execute(f'''
                   UPDATE lojas
                    SET nome = '{novo_nome}', endereco = '{novo_endereco}', id_rede = {novo_id_rede}  WHERE id = {id_loja}''')
    conexao.commit()
    print("Dados atualizados com sucesso! ")
    conexao.close()

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

def menu_principal():
    try:
        acao = 0
        while True:
            print(" SISTEMA DE MERCADOS PARANAVAÍ")
            print("==================================\n 1 - MENU DE REDES\n 2 - MENU DE LOJAS\n 3 - ENCERRAR SISTEMA\n==================================\n")
            acao = int(input("Digite a opção do menu para acessar: "))
            if acao == 1:
                menu_redes()
            elif acao == 2:
                menu_lojas()
            elif acao == 3:
                break
            elif acao not in (1, 2, 3):
                print("Insira uma opção válida")
        print("Volte sempre!")
        
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    finally:
        if acao != 3:
            print("Tente novamente")
            menu_principal()
        elif acao == 3:
            print("Fechando menu principal")
        else:
            menu_principal()




menu_principal()