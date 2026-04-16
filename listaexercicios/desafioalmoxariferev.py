print("\nVocê pode adicionar e listar itens aqui, basta inserir abaixo: ")
estoque = []
print("\nestoque: ", estoque)
acao = ""
while acao != "Finalizar":
    acao = input("\nQual ação deseja realizar ?(Adicionar/Listar/Finalizar): ")
    if acao == "Adicionar":
        item = input("Digite um item: ")
        estoque.append(item)
        print(f"\nitem {item} adicionado")
    elif acao == "Listar":
        print("O estoque atual é:", estoque)
print("Operação finalizada, estoque final: ", estoque)
