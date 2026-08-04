import sqlite3 
id_prof = int(input("Digite o id do professor: "))
def buscar_professor(id_prof): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor()

	# O Python reclama de "Incorrect number of bindings".  
	# Estamos passando a variável, por que ocorre o erro? 
    cursor.execute(f"SELECT nome FROM professores WHERE id = {id_prof}") 
    resultado = cursor.fetchone() 
    print(resultado) 
    conexao.close() 

buscar_professor(id_prof)