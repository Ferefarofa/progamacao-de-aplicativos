valor = float(input("Qual o valor da compra?: "))
ass = input("É assinante prime? (Sim/Nao): ")
frete = 50.00
if valor >= 500 or ass == "Sim" and valor >= 100:
    frete = 0.00

valorfinal = valor + frete
print("Frete: ", frete)
print("Total a pagar: ", valorfinal)
