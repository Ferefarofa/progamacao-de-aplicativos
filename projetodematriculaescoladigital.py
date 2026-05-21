import json

def criar_arquivo():
    open("matriculas.json", 'w').close()
    with open("matriculas.json", 'w') as matriculas:
        dados = {"cpf": ["Sem dados"],
                "nome": ["Sem dados"],
                "telefone": ["Sem dados"],
                "turma": ["Sem dados"],
                "idade": ["Sem dados"]
                }
        json.dump(dados, matriculas, indent=4, ensure_ascii=False)
        
def cadastrar_aluno():
    with open("matriculas.json", 'r') as matriculas:
        dados = json.load(matriculas)
    cpf = input("Digite o CPF do aluno: ")
    if cpf in dados["cpf"]:
        print("CPF já existe ")
    else:
        nome = input("Digite o nome do aluno: ")
        telefone = input("Digite o telefone do aluno: ")
        turma = input("Digite a turma do aluno: ")
        idade = input("Digite a idade do aluno: ")
        dados["cpf"].append(cpf)
        dados["nome"].append(nome)
        dados["telefone"].append(telefone)
        dados["turma"].append(turma)
        dados["idade"].append(idade)
        with open("matriculas.json", 'w') as matriculas:
            json.dump(dados, matriculas, indent=4, ensure_ascii=False)

def listar():
    quem = input("Digite o cpf que deseja verificar: ")
    with open("matriculas.json", 'r') as matriculas:
        dados = json.load(matriculas)
        idx = dados["cpf"].index(quem)
    print(f"{dados["cpf"][idx], dados["nome"][idx], dados["telefone"][idx], dados["turma"][idx], dados["idade"][idx]}")

def atualizar():
    quem = input("Insira o cpf a ser alterado: ")
    mudar = input("Insira o campo a ser atualizado: ")
    mudanca = input("Insira o novo dado: ")
    if mudar == "cpf":
        print("Não é possível mudar o cpf de cadastro. ")
    else:
        with open("matriculas.json", 'r') as matriculas:
            dados = json.load(matriculas)
            dados[quem][mudar] = mudanca

        with open("matriculas.json", 'w') as matriculas:
            json.dump(dados, matriculas, indent=4, ensure_ascii=False)

def remover():
    quem = input("Digite o cpf a ser removido")

