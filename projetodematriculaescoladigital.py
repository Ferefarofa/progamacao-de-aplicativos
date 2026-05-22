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
    print("Arquivo criado com sucesso!")
        
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
    print(f"CPF:{dados["cpf"][idx]}\nNome:{dados["nome"][idx]}\nTelefone:{dados["telefone"][idx]}\nTurma:{dados["turma"][idx]}\nIdade:{dados["idade"][idx]}\n")

def atualizar():
    quem = input("Insira o CPF a ser alterado: ")
    mudar = input("Insira o campo a ser atualizado: ")
    if mudar == "cpf":
        print("Não é possível mudar o cpf de cadastro. ")
        
    else:
        mudanca = input("Insira o novo dado: ")
        with open("matriculas.json", 'r') as matriculas:
            dados = json.load(matriculas)
            idx = dados["cpf"].index(quem)
            dados[mudar][idx] = mudanca
        with open("matriculas.json", 'w') as matriculas:
            json.dump(dados, matriculas, indent=4, ensure_ascii=False)
        print("Dado atualizado com sucesso! ")

def remover():
    quem = input("Digite o cpf a ser removido: ")
    confirmar = input("Confirmação:\n Para remover a matricula do sistema digite DELETAR, caso contrário digite algo diferente: ")
    if confirmar != "DELETAR":
        print("Remoção de matrícula cancelada. ")
    elif confirmar == "DELETAR":
        with open("matriculas.json", 'r') as matriculas:
            dados = json.load(matriculas)
        idx = dados["cpf"].index(quem)
        del dados["cpf"][idx]
        del dados["nome"][idx]
        del dados["telefone"][idx]
        del dados["turma"][idx]
        del dados["idade"][idx]
        with open("matriculas.json", 'w') as matriculas:
            json.dump(dados, matriculas, indent=4, ensure_ascii=False)
        print("Matrícula removida com sucesso! Até mais...")

while True:
    senha = "1e2e3"
    print("-------------Sistema de matriculas-------------")
    print("OPÇÕES\n")
    print("1-Cadastrar aluno\n 2-Dados da matrícula\n 3-Atualizar dados\n 4-Remover matrícula\n 5-Fechar programa\n 6-Criar arquivo\n")
    opcao = int(input("Digite a ação: "))

    if opcao == 1:
        cadastrar_aluno()
    elif opcao == 2:
        listar()
    elif opcao == 3:
        atualizar()
    elif opcao == 4:
        remover()
    elif opcao == 5:
        break
    elif opcao == 6:
        chave = input("Digite a senha: ")
        if chave == senha:
            criar_arquivo()
        else:
            print("Ação negada.")
print("Programa encerrado. ")