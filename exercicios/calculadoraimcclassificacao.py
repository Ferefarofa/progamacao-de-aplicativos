def gerar_relatorio_saude(nome, peso, altura, idade):
    imc = peso / (altura ** 2)
    if imc < 18.5:
        resultado = "Baixo peso"
    elif imc >= 18.5 and imc <= 24.9:
        resultado = "Peso ideal"
    elif imc >= 25 and imc <= 29.9:
        resultado = "Sobrepeso"
    elif imc >= 30:
        resultado = "Obesidade"
    print(f"O imc de {nome} é {imc} e sua idade é {idade}, o resultado do exame indica {resultado}.")
nome_alt = input("Qual o seu nome ?: ")
peso_alt = float(input("Insira o seu peso em kg: "))
altura_alt = float(input("Insira sua altura em metros: "))
idade_alt = input("Insira a sua idade: ")
gerar_relatorio_saude(nome_alt, peso_alt, altura_alt, idade_alt)
