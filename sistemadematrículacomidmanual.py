import json
import os

BANCO_DADOS = 'alunes.json'

def cadastrar_aluno():
    if os.path.exists(BANCO_DADOS):
        with open("alunes.json", 'r') as alunes:
            alunos = json.load(alunes)
    else:
        alunos = []
    
    novo_aluno = {
        "id": int(input("Digite o ID do aluno: ")),
        "nome": input("Digite o nome do aluno: "),
        "telefone": input("Digite o telefone do aluno: "),
        "turma": input("Digite a turma do aluno: "),
        "idade": input("Digite a idade do aluno: "),
        "cpf": input("Digite o cpf do aluno: ")
    }
    alunos.append(novo_aluno)
    with open(BANCO_DADOS, 'w') as alunes:
        json.dump(alunos, alunes, indent=4, ensure_ascii=False)
    
    print("Aluno adicionado com sucesso: ")

def listar():
    with open(BANCO_DADOS, 'r') as alunes:
        alunos = json.load(alunes)
    idx = int(input("Digite o ID do aluno a ser pesquisado: "))
    aluno = alunos
    