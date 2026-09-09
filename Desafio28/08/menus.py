import sqlite3
conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")
from banco import criar_tabela_escolas, criar_tabela_turmas, criar_tabela_alunos, hello_gestao_escolar
from escolas import cadastrar_escola, listar_escolas, atualizar_escola, remover_escola
from turmas import cadastrar_turma, listar_turmas, atualizar_turma, remover_turma
from alunos import cadastrar_aluno, listar_alunos, atualizar_aluno, remover_aluno


hello_gestao_escolar()
def menu_escolas():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        
        opcao = 0
        while opcao != 5:
            print("==================================\n 1 - CADASTRAR ESCOLA\n 2 - LISTAR ESCOLAS\n 3 - ATUALIZAR ESCOLA\n 4 - REMOVER ESCOLA\n 5 - SAIR\n==================================")
            opcao = int(input("Digite sua ação: "))
            if opcao == 1:
                cadastrar_escola()
            elif opcao == 2:
                listar_escolas()
            elif opcao == 3:
                atualizar_escola()
            elif opcao == 4:
                remover_escola()
            elif opcao == 5:
                break
            elif opcao not in (1, 2, 3, 4, 5):
                print("Insira uma opção válida")
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    finally:
        if opcao != 5:
            print("Tente novamente")
            menu_escolas()
        elif opcao == 5:
            print("Fechando menu das escolas")
            conexao.close()
        else:
            menu_escolas()


def menu_turmas():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        
        opcao = 0
        while opcao != 5:
            print("==================================\n 1 - CADASTRAR TURMA\n 2 - LISTAR TURMAS\n 3 - ATUALIZAR TURMA\n 4 - REMOVER TURMA\n 5 - SAIR\n==================================")
            opcao = int(input("Digite sua ação: "))
            if opcao == 1:
                cadastrar_turma()
            elif opcao == 2:
                listar_turmas()
            elif opcao == 3:
                atualizar_turma()
            elif opcao == 4:
                remover_turma()
            elif opcao == 5:
                break
            elif opcao not in (1, 2, 3, 4, 5):
                print("Insira uma opção válida")
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    finally:
        if opcao != 5:
            print("Tente novamente")
            menu_turmas()
        elif opcao == 5:
            print("Fechando menu das turmas")
            conexao.close()
        else:
            menu_turmas()


def menu_alunos():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        
        opcao = 0
        while opcao != 5:
            print("==================================\n 1 - CADASTRAR ALUNO\n 2 - LISTAR ALUNOS\n 3 - ATUALIZAR ALUNO\n 4 - REMOVER ALUNO\n 5 - SAIR\n==================================")
            opcao = int(input("Digite sua ação: "))
            if opcao == 1:
                cadastrar_aluno()
            elif opcao == 2:
                listar_alunos()
            elif opcao == 3:
                atualizar_aluno()
            elif opcao == 4:
                remover_aluno()
            elif opcao == 5:
                break
            elif opcao not in (1, 2, 3, 4, 5):
                print("Insira uma opção válida")
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    finally:
        if opcao != 5:
            print("Tente novamente")
            menu_alunos()
        elif opcao == 5:
            print("Fechando menu dos alunos")
            conexao.close()
        else:
            menu_alunos()

        
def menu_gestao_escolar():
    conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")
    try:
        acao = 0
        while True:
            print(" SISTEMA GESTOR DE ESCOLAS DE PARANAVAÍ")
            print("==================================\n 1 - MENU DAS ESCOLAS\n 2 - MENU DAS TURMAS\n 3 - MENU DOS ALUNOS\n 4 - ENCERRAR SISTEMA\n==================================\n")
            acao = int(input("Digite a opção do menu para acessar: "))
            if acao == 1:
                menu_escolas()
            elif acao == 2:
                menu_turmas()
            elif acao == 3:
                menu_alunos()
            elif acao == 4:
                break
            elif acao not in (1, 2, 3, 4):
                print("Insira uma opção válida")
        print("Volte sempre!")
        
    except ValueError:
        print("Não digite letras em campos numéricos e vice-versa")
    finally:
        if acao != 4:
            print("Tente novamente")
            menu_gestao_escolar()
        elif acao == 4:
            print("Fechando menu principal")
            conexao.close()
        else:
            menu_gestao_escolar()

menu_gestao_escolar()