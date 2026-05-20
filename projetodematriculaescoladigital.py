import json

def criar_arquivo():
    open("matriculas.json", 'w').close()
    with open("matriculas.json", 'w') as matriculas:
        dados = {"CPF": "Sem dados",
                "nome": "Sem dados",
                "telefone": "Sem dados",
                "turma": "Sem dados",
                "idade": "Sem dados"
                }
        json.dump(dados, matriculas, indent=4, ensure_ascii=False)
        
def cadastrar_aluno():
    cpf = int(input("Digite o CPF do aluno: "))
    nome = input("Digite o nome do aluno: ")
    telefone = int(input("Digite o telefone do aluno: "))
    turma = input("Digite a turma do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    with open("matriculas.json", 'r') as matriculas:
        dados = json.load(matriculas)
        if dados["CPF"] == cpf:
            print("CPF já existe ")
        else:
            dados["CPF"] = cpf
            dados["nome"] = nome
            dados["telefone"] = telefone
            dados["turma"] = turma
            dados["idade"] = idade

def listar():
    with open("matriculas.json", 'r') as matriculas:
        dados = json.load(matriculas)
    print(f"{dados}")
