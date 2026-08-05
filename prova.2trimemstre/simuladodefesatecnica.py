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


        
        comando_inserir_academia = " INSERT INTO hoteis(nome, cidade) VALUES(?, ?)"
        comando_inserir_alunos = " INSERT INTO quartos(numero, preco_diaria, id_hotel) VALUES(?, ?, ?)"

        cursor.execute(comando_inserir_academia, (nome_unidade, bairro))
        cursor.execute(comando_inserir_alunos, (nome_aluno, mensalidade, id_academia))
        conexao.commit()

        
    except sqlite3.IntegrityError:
        print("Erro, id da academia inválido.")

    finally:

        conexao.close()



def listar():

    
    conexao = sqlite3.connect('prova.2trimemstre/banco_hotelaria.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    cursor.execute('''SELECT * FROM salas''')

    salas = cursor.fetchall()

    for sala in salas:
        print(f"===============================================\n ID Sala: {sala[0]}\n Numero da Sala: {sala[1]}\n Capacidade: {sala[2]}\n ID Cinema: {sala[3]}\n===============================================" )
