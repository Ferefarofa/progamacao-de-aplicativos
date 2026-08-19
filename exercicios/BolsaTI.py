print("Para ver se você atende os requisitos para a bolsa, preencha os dados a seguir: ")
media = float(input("Qual a sua média?: "))
renda = float(input("Qual a sua renda familiar?: "))
escola = input("Vem de escola pública?(Sim/Nao): ")
if media >= 8.0 and renda <= 2000.00 or escola == ("Sim"):
    print("Ganhou a bolsa")
else:
    print("Não atende aos requisitos")
