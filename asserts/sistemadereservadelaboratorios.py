import sqlite3
conexao = sqlite3.connect('reservas.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
 
def laboratorios():
    conexao = sqlite3.connect('reservas.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS informatica01(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_solicitante TEXT NOT NULL,
                    data TEXT UNIQUE NOT NULL,
                    horario TEXT NOT NULL
                    )''')


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS informatica02(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_solicitante TEXT NOT NULL,
                    data TEXT UNIQUE NOT NULL,
                    horario TEXT NOT NULL
                    )''')


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS robotica(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_solicitante TEXT NOT NULL,
                    data TEXT UNIQUE NOT NULL,
                    horario TEXT NOT NULL
                    )''')


    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS eletronica(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome_solicitante TEXT NOT NULL,
                    data TEXT UNIQUE NOT NULL,
                    horario TEXT NOT NULL
                    )''')

    
    conexao.commit()
    conexao.close()

def reservar():
    conexao = sqlite3.connect('reservas.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    print("\n================================\n Laboratórios:\n informática01\n informatica02\n robótica\n eletrôncia\n================================")
    
    nome_solicitante = input("Insira o nome do solicitante: ")
    laboratorio = input("Insira o nome do laboratório da reserva: ")
    data = input("Insira a data da reserva: ")
    horario = input("Insira o horário da reserva: ")
    
    cursor.execute(f'''
                    INSERT INTO {laboratorio}(nome_solicitante, data, horario) VALUES('{nome_solicitante}', '{data}',  '{horario}')
                    ''')
    conexao.commit()
    conexao.close()


def consultar():
    print("\n================================\n Laboratórios:\n informática01\n informatica02\n robótica\n eletrôncia\n================================")
    laboratorio = input("Digie o laboratorio a ser consultado: ")
    cursor.execute(f"SELECT * FROM {laboratorio}")
    resultado = cursor.fetchall()
    for item in resultado:
        print(f"================================\n Solicitante:{item[1]}\n Data:{item[2]}\n Horário:{item[3]}\n================================")











