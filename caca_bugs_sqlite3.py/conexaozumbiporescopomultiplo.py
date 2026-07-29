import sqlite3 
 
# O aluno criou a conexão fora das funções para "facilitar". 
# Por que isso quebra o sistema quando usamos múltiplos arquivos (módulos)? 
conexao = sqlite3.connect('sistema_escola.db') 
cursor = conexao.cursor() 
 
def inserir_escola(nome): 
    conexao = sqlite3.connect('sistema_escola.db') 
    cursor = conexao.cursor() 
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,)) 
    conexao.commit() 

nome = input("Digite o nome da escola: ")
inserir_escola(nome)
#é tipo como e a conexao criada fora da fução fechasse tudo porque é usada de forma geral, ja uma conexao close criada dentro da função fecha apenas a conexão abrida dentro dela.