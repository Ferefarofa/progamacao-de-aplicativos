peso = float(input("Qual o seu peso ?: "))
altura = float(input("Qual a sua altura ?: "))
imc = peso / (altura**2)
if imc > 25:
    print("Está gorde")
elif imc <= 25:
    print("Tá bão")