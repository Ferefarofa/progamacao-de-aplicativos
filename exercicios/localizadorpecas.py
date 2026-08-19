ferramentas = ["Chave Inglesa", "Alicate", "Martelo", "Parafusadeira"]
perg = input("Qual ferramenta você procura ?: ")
for ferramenta in ferramentas:
    if perg == ferramenta:
        print(f"\nFerramenta {ferramenta} encontrada no índice {ferramentas.index(ferramenta)}")
while perg in ferramentas:
    perg = input("Qual ferramenta você procura ?: ")
    for ferramenta in ferramentas:
        if perg == ferramenta:
            print(f"\nFerramenta {ferramenta} encontrada no índice {ferramentas.index(ferramenta)}")
else:
    pregunta = input("Ferramenta não encontrada, deseja adiciona-la a caixa de ferramentas ?(S/N): ")
    if pregunta == "S":
        ferramentas.append(perg) 
        while pregunta != "N":
            pregunta = input("Ferramenta adicionada! Deseja adicionar mais alguma?(S/N) : ")
            if pregunta == "S":
                outra = input("Qual ferramenta?: ")
                ferramentas.append(outra)
    if pregunta == "N":
        print(f"ferramentas disponiveis: {ferramentas}")

