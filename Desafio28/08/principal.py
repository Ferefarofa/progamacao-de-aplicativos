import sqlite3
conexao = sqlite3.connect('Desafio28/08/gestao_escolar.db')
cursor = conexao.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

from banco import criar_tabela_escolas, criar_tabela_turmas, criar_tabela_alunos, hello_gestao_escolar
from escolas import cadastrar_escola, listar_escolas, atualizar_escola, remover_escola
from turmas import cadastrar_turma, listar_turmas, atualizar_turma, remover_turma
from alunos import cadastrar_aluno, listar_alunos, atualizar_aluno, remover_aluno
from menus import menu_escolas, menu_turmas, menu_alunos, menu_gestao_escolar

hello_gestao_escolar()
menu_gestao_escolar()