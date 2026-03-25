autorizados =  ["Alice", "Bob", "Carlos"]
nome = input("\nDigite o nome do pesquisador: ")
if nome in autorizados:
    print(f"\nAcesso Permitido! O pesquisador {nome} está na posição",autorizados.index(nome)) 
    pergunta = input("\nVocê quer remover o nome da lista ?(Sim/Não): ")
    if pergunta == "Sim":
        autorizados.remove(nome)
        print(f"\nAgora os membros da lista são {autorizados}")
    else:
        print("Encerrando programa...")
else:
    print(f"\nAcesso Negado! O pesquisador {nome} não foi encontrado.")
    perg2 = input("\nQuer cadastrar esse nome como novo pesquisador ?(Sim/Não): ")
    if perg2 == "Sim":
        autorizados.append(nome)
        print(f"\nAgora os membros da lista são: {autorizados}")
