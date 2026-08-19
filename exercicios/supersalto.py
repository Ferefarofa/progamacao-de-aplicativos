print("Você deve atender os requisitos para conseguir usar a habilidade super salto, preencha os dados a seguir para desbloquear: ")
print(" ")
nivel = int(input("Qual o seu nível ?: "))
esferas = int(input("Quantas eseferas de energia você tem ?: "))
if nivel >= 20 and esferas >= 50:
    print("Habilidade Super Salto desbloqueada!")
else:
    print("Requisitos insuficientes para nova habilidade.")
    