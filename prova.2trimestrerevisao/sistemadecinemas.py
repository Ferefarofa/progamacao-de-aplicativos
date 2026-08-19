import sqlite3
conexao = sqlite3.connect('prova.2trimemstre/banco_cinema.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
def cadastro():
    try:
        conexao = sqlite3.connect('prova.2trimemstre/banco_cinema.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")


        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS cinemas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_cinema TEXT NOT NULL,
                        shopping TEXT NOT NULL
                    )
                    ''')

        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS salas(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        numero_sala INTEGER NOT NULL,
                        capacidade INTEGER NOT NULL,
                        id_cinema INTEGER NOT NULL,
                        FOREIGN KEY (id_cinema) REFERENCES cinemas(id)
                    )
        ''')


        confirmar = ""
        while confirmar != "S":
            nome_cinema = input("Digite o nome do cinema: ")
            shopping = input("Digite o nome do shopping do cinema: ")
            numero_sala = int(input("Digite o numero da sala: "))
            capacidade = int(input("Digite a capacidade da sala: "))
            id_cinema = int(input("Digite o id do cinema: "))
            print(f"==================================\n Nome do cinema: {nome_cinema}\n Shopping: {shopping}\n Número da sala(a): {numero_sala}\n Capacidade: {capacidade}\n ID cinema: {id_cinema}\n==================================\n Confira as informações.")
            confirmar = input("Prosseguir ?(S/N): ")


        
        comando_inserir_cinema = f''' INSERT INTO cinemas(nome_cinema, shopping) VALUES('{nome_cinema}', '{shopping}')'''
        comando_inserir_sala = f''' INSERT INTO salas(numero_sala, capacidade, id_cinema) VALUES({numero_sala}, {capacidade}, {id_cinema})'''

        cursor.execute(comando_inserir_cinema)
        cursor.execute(comando_inserir_sala)
        conexao.commit()

        
    except sqlite3.IntegrityError:
        print("Erro, id do cinema inválido.")

    finally:

        conexao.close()
    

def listar():

    
        conexao = sqlite3.connect('prova.2trimemstre/banco_cinema.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute('''SELECT * FROM salas''')

        salas = cursor.fetchall()

        for sala in salas:
            print(f"===============================================\n ID Sala: {sala[0]}\n Numero da Sala: {sala[1]}\n Capacidade: {sala[2]}\n ID Cinema: {sala[3]}\n===============================================" )



listar()























