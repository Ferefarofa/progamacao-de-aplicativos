def avaliar_desempenho(nota):
    if nota >= 9:
        print("Excelente!!! ")
    elif nota >= 7:
        print("Bom!")
    elif nota >= 5:
        print("Regular")
    else:
        print("Insuficiente.")
nota = float(input("Insira a sua nota: "))
avaliar_desempenho(nota)

