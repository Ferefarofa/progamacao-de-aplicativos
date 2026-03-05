comprimento = (input("O comprimento da peça está entre 10 e 12 cm?(s/n): "))
if comprimento == "n":
    print("REPROVADO: Problema no comprimento")
elif comprimento == "s":
    largura = input("A largura está entre 5 e 6 cm ?(s/n): ")
    if largura == "s":
        print("PEÇA APROVADA.")
    elif largura == "n":
        print("REPROVADO:problema na largura.")
