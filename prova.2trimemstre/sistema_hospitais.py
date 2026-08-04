import sqlite3
conexao = sqlite3.connect('prova.2trimemstre/banco_hospital.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
def cadastro():
    try:
        conexao = sqlite3.connect('prova.2trimemstre/banco_hospital.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")


        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS hospitais(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cidade TEXT NOT NULL
                    )
                    ''')

        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS medicos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        crm INTEGER UNIQUE NOT NULL,
                        id_hospital INTEGER NOT NULL,
                        FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
                    )
        ''')


        confirmar = ""
        while confirmar != "S":
            nome = input("Digite o nome do hospital: ")
            cidade = input("Digite o nome da cidade do hospital: ")
            nome_medico = input("Digite o nome do médico: ")
            crm = int(input("Digite o crm do médico: "))
            id_hospital = int(input("Digite o id do hospital: "))
            print(f"==================================\n Nome do hopital: {nome}\n Cidade: {cidade}\n Medico(a): {nome_medico}\n CRM: {crm}\n ID hospital: {id_hospital}\n==================================\n Confira as informações.")
            confirmar = input("Prosseguir ?(S/N): ")


        
        comando_inserir_hospital = f''' INSERT INTO hospitais(nome, cidade) VALUES('{nome}', '{cidade}')'''
        comando_inserir_medicos = f''' INSERT INTO medicos(nome, crm, id_hospital) VALUES('{nome_medico}', {crm}, {id_hospital})'''

        cursor.execute(comando_inserir_hospital)
        cursor.execute(comando_inserir_medicos)
        conexao.commit()

        
    except sqlite3.IntegrityError:
        print("Erro, id do hospital inválido.")

    finally:

        conexao.close()
    

cadastro()

