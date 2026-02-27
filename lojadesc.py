valort = float(input("Qual o valor total da compra ?: "))
cupom = input("Digite o seu cupom: ")

if cupom == "DEV10":
    desc = valort * 0.10
    valord = valort - desc
    print("O novo valor atual é: ", valord)
else:
    print("Cupom inválido, valor original ", valort)
    