import sqlite3
conexao = sqlite3.connect('prova.2trimemstre/banco_hotelaria.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
def cadastro():
    try:
        conexao = sqlite3.connect('prova.2trimemstre/banco_hotelaria.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("PRAGMA encoding = 'UTF-8'")


        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS hoteis(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cidade TEXT NOT NULL
                    )
                    ''')

        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS quartos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero INTEGER NOT NULL,
                        preco_diaria INTEGER NOT NULL,
                        id_hotel INTEGER NOT NULL,
                        FOREIGN KEY (id_hotel) REFERENCES hoteis(id)
                    )
        ''')


        confirmar = ""
        while confirmar != "S":
            nome = input("Digite o nome do hotel: ")
            cidade = input("Digite o nome da cidade do hotel: ")
            numero = int(input("Digite o número do quarto: "))
            preco_diaria = int(input("Digite o preco da diaria: "))
            id_hotel = int(input("Digite o id do hotel: "))
            print(f"==================================\n Nome do hotel: {nome}\n Cidade: {cidade}\n Numero do quarto: {numero}\n Preço da diária: {preco_diaria}\n ID hotel: {id_hotel}\n==================================\n Confira as informações.")
            confirmar = input("Prosseguir ?(S/N): ")


        
        comando_inserir_hotel = " INSERT INTO hoteis(nome, cidade) VALUES(?, ?)"
        comando_inserir_quarto = " INSERT INTO quartos(numero, preco_diaria, id_hotel) VALUES(?, ?, ?)"

        cursor.execute(comando_inserir_hotel, (nome, cidade))
        cursor.execute(comando_inserir_quarto, (numero, preco_diaria, id_hotel))
        conexao.commit()

        
    except sqlite3.IntegrityError:
        print("Erro, id do hotel inválido.")

    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    finally:

        conexao.close()



def listar():

    
    conexao = sqlite3.connect('prova.2trimemstre/banco_hotelaria.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('''SELECT * FROM quartos''')

    quartos = cursor.fetchall()

    for quarto in quartos:
        print(f"==================================\n ID Quarto: {quarto[0]}\n Numero do Quarto: {quarto[1]}\n Preço da diária: {quarto[2]}\n ID Hotel: {quarto[3]}\n==================================" )



def menu():
    try:
        opcao = 1
        while opcao != 3:
            print("==================================\n 1 - CADASTRAR HOSPEDE\n 2 - LISTAR HOSPEDES\n 3 - SAIR\n==================================")
            opcao = int(input("Digite sua ação: "))
            if opcao == 1:
                cadastro()
            elif opcao == 2:
                listar()
            elif opcao == 3:
                break
            elif opcao != 1 or 2 or 3:
                print("Insira uma opção válida")
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
        pass
    finally:
        if opcao != 2:
            print("Tente novamente")
            menu()
        elif opcao == 3:
            break
        else:
            menu()


        
            

menu()
print("Volte sempre!")