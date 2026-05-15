def criar_mural():
    open('mural_habitos.txt', 'w').close
    print("\nMural de bons hábitos criados! ")

def adicionar_habito():
    habito = input("\nDigite um bom hábito para adicionar: ")
    with open('mural_habitos.txt', 'a') as mural:
        mural.write(habito + "\n")
        print("\nHábito adicionado com sucesso! ")

def listagem():
    print("Hábitos adicionados: ")
    with open('mural_habitos.txt', 'r') as mural:
        habitos = mural.readlines()
        i = 0
        for habito in habitos:
            print(f"{i} - {habito.strip()}")
            i += 1

def substituir_habito():
    