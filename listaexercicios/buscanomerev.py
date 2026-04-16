nomes = ["felipe", "isadora", "joão", "gustavo", "duda"]
perg = (input("Digite um nome para ver se ele está na lista: "))
if perg in nomes:
    print("Nome está na lista")
elif perg not in nomes:
    print("Nome não está na lista")