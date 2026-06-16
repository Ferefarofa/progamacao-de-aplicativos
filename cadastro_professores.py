import sqlite3
conexao = sqlite3.connect('escola.demosntracao.db')
cursor = conexao.cursor()



def cadastrar_professor():

    nome_professor = input("Digite o nome do professor: ")
    telefone_professor = input("Digite o telefone do professor: ")
    materia = input("Digite a matéria do professor: ")
    idade_professor = int(input("Digite a idade do professor: "))
    cpf_professor = input("Digite o CPF do professor: ")
    salario = input("Digite o salario do professor: ")
    nome_da_escola = input("Digite o nome da escola: ")

    cursor.execute('''CREATE TABLE IF NOT EXISTS professores(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nome TEXT NOT NULL,
                   telefone TEXT,
                   materia TEXT,
                   idade INTEGER,
                   cpf TEXT UNIQUE NOT NULL,
                   salario TEXT,
                   nome_escola TEXT NOT NULL)''')
    
    comando_inserir = f'''
        INSERT INTO professores(nome, telefone, materia, idade, cpf, salario, nome_escola)
        VALUES('{nome_professor}', '{telefone_professor}', '{materia}', 
        '{idade_professor}', '{cpf_professor}', '{salario}', '{nome_da_escola}')'''
    
    cursor.execute(comando_inserir)
    conexao.commit()

def listar_professores():

    cursor.execute("SELECT * FROM professores")
    todos_professores = cursor.fetchall()
    if not todos_professores:
        print("Nenhum professor cadastrado. ")

    else:
        for professor in todos_professores:
            print(f"{professor[0]}, nome:{professor[1]}, telefone:{professor[2]}, materia:{professor[3]}, idade:{professor[4]}, CPF:{professor[5]}, salario:{professor[6]}, escola:{professor[7]}")
    print("\n")
    if not professor:
        print("Nenhum professor cadastrado. ")

def atualizar_dados():
    id_professor = int(input("Digite o ID do professor: "))
    novo_nome_professor = input("Digite o novo nome d professor: ")
    novo_telefone_professor = input("Digite o novo telefone do professor: ")
    nova_materia = input("Digite a nova materia do professor: ")
