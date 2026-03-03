idade = int(input("Qual a sua idade?: "))
ingresso = input("Possui o ingresso ? (Sim/Nao): ")
convite = input("É convidado ? (Sim/Nao) ")
if (idade >= 18 and ingresso == "Sim") or convite == "Sim":
    print("Entrada permitida, Bem vindo! ")
else:
    print("Entrada negada.")
