def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    aprovado = False
    if (nota_teste >= 80 and anos_xp > 2) or possui_certificacao == "S":
        aprovado = True
    if aprovado == True:
        print("Contratar. ")
    elif aprovado == False:
        print("Descartar. ")
nota = float(input("Qual a nota teste ?: "))
anos_exp = int(input("Quantos anos de experiência o candidato possui ?: "))
certificado = input("Possui certificado ?(S/N): ")
verificar_aprovacao(nota, anos_exp, certificado)