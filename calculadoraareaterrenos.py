acoes = 3
def calcular_area(largura, comprimento):
    area = largura * comprimento
    print(f"A área calculada do terreno é de {area}m²")
while acoes != 0:
    print("Para calcular a área do terreno insira a sua largura e seu comrpimento: ")
    largura = int(input("Insira a largura do terreno: "))
    comprimento = int(input("Insira o comrpimento do terreno: "))
    calcular_area(largura, comprimento)
    acoes -= 1
    print(f"Ações restantes: {acoes}")
print("Programa encerrado.")
