import sqlite3
conexao = sqlite3.connect('prova.2trimemstre/banco_academia.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
def cadastro():
    try:
        conexao = sqlite3.connect('prova.2trimemstre/banco_academia.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute("PRAGMA encoding = 'UTF-8'")


        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS academias(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_unidade TEXT NOT NULL,
                        bairro TEXT NOT NULL
                    )
                    ''')

        cursor.execute('''
                        CREATE TABLE IF NOT EXISTS alunos(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        mensalidade INTEGER NOT NULL,
                        id_academia INTEGER NOT NULL,
                        FOREIGN KEY (id_academia) REFERENCES academias(id)
                    )
        ''')


        confirmar = ""
        while confirmar != "S":
            nome_unidade = input("Digite o nome da academia: ")
            bairro = input("Digite o nome do bairro da academia: ")
            nome_aluno = input("Digite o nome do aluno: ")
            mensalidade = int(input("Digite a mensalidade da adademia: "))
            id_academia = int(input("Digite o id da academia: "))
            print(f"==================================\n Nome da academia: {nome_unidade}\n Bairro: {bairro}\n Nome do aluno(a): {nome_aluno}\n Mensalidade: {mensalidade}\n ID academia: {id_academia}\n==================================\n Confira as informações.")
            confirmar = input("Prosseguir ?(S/N): ")


        
        comando_inserir_academia = " INSERT INTO academias(nome_unidade, bairro) VALUES(?, ?)"
        comando_inserir_alunos = " INSERT INTO alunos(nome, mensalidade, id_academia) VALUES(?, ?, ?)"

        cursor.execute(comando_inserir_academia, (nome_unidade, bairro))
        cursor.execute(comando_inserir_alunos, (nome_aluno, mensalidade, id_academia))
        conexao.commit()

        
    except sqlite3.IntegrityError:
        print("Erro, id da academia inválido.")

    finally:

        conexao.close()
    

cadastro()

