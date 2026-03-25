compras = []
while compras != "fim":
    item = input("Item a ser adicionado na lista: ")
    compras.append(item)
if compras == "fim":
    print("Inserção de itens finalizada, lista final: ", compras)