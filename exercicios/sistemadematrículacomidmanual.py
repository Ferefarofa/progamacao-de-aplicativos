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
        "id": input("Digite o ID do aluno: "),
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
    if os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'r') as alunes:
            alunos = json.load(alunes)
        for aluno in alunos: 
            print(f"ID: {aluno["id"]}\nNome: {aluno["nome"]}\nTelefone: {aluno["telefone"]}\nTurma: {aluno["turma"]}\nIdade: {aluno["idade"]}\nCPF: {aluno["cpf"]}")
            print("---------------------------------------------------")
    else:
        print("Nenhum aluno cadastrado! ")

def atualizar():
    if os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'r') as alunes:
            alunos = json.load(alunes)
        
        idx = input("Digite o ID do aluno que deseja alterar os dados: ")
        campo = input("Digite o campo que deseja alterar: ")
        if campo != "id":
            for aluno in alunos:
                if aluno["id"] == idx:
                    aluno[campo] = input("Digite o novo dado: ")
                    with open(BANCO_DADOS, 'w') as alunes:
                        json.dump(alunos, alunes, indent=4, ensure_ascii=False)
                        print("Dados atualizados com sucesso! ")
        else:
            print("Você não pode alterar o ID do aluno. ")
    else:
        print("Nenhum aluno para atualizar. ")


def remover():
    if os.path.exists(BANCO_DADOS):
        with open(BANCO_DADOS, 'r') as alunes:
            alunos = json.load(alunes)
        
        idx = input("Digite o ID do aluno que deseja remover do registro: ")
        for aluno in alunos:
            if aluno["id"] == idx:
                del alunos[aluno]
            with open(BANCO_DADOS, 'w') as alunes:
                json.dump(alunos, alunes, indent=4, ensure_ascii=False)
                print("Aluno removido. ")

remover()