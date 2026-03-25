livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "Hardware"]
livros_emprestados = []
perg = input("\nQual livro você deseja emprestar ?: ")
if perg in livros_disponiveis:
    livros_emprestados.append(perg)
    livros_disponiveis.remove(perg)
    print("\nEmpréstimo concluído, Boa Leitura!")
    print("\nAgora o status das listas são: ")
    print(f"livros disponíveis: {livros_disponiveis}")
    print(f"livros emprestados {livros_emprestados}")
else:
        print("\nDesculpe, este livro não está no acervo.")

perg2 = input("Qual livro você deseja devolver: ")
if perg in livros_emprestados:
    livros_disponiveis.append(perg2)
    livros_emprestados.remove(perg2)
    print("\nLivro devolvido com sucesso !")
    print("\nAgora o status das listas são: ")
    print(f"livros disponíveis: {livros_disponiveis}")
    print(f"livros emprestados {livros_emprestados}")
else:
    print("\nDesculpe, este livro não está no acervo.")
print("\nManuntenção de acervo !")
del livros_disponiveis[0:2]
print(f"Lista atual de livros disponíveis: {livros_disponiveis}")


