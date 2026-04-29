def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    aprovado = False
    possui_certificacao = False
    if possui_certificacao == "Sim":
        possui_certificacao = True
    if nota_teste > 80 and anos_xp > 2 or possui_certificacao == True:
        aprovado = True
    if aprovado == True:
        print("Contratar. ")
    else:
        print("Descartar. ")
nota = float(input(""))