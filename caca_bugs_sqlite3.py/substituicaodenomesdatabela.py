import sqlite3 
 
def buscar_dados_dinamicos(nome_tabela, id_registro): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
     
	# O SQLite joga um erro de sintaxe operacional indicando que não aceita o caractere '?'. 
	# Não podemos parametrizar nomes de tabelas? Como resolver mantendo a segurança? 
    cursor.execute(f"SELECT * FROM {nome_tabela} WHERE id = ?", (id_registro, )) 
     
    print(cursor.fetchone()) 
    conexao.close() 

nome_tabela = input("Digite o nome da tabela: ")
id_registro = input("Digite o id de registro: ")
buscar_dados_dinamicos(nome_tabela, id_registro)