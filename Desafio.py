print("O sistema deve calcular o preço final, e decidir se o cliente tem direito a frete grátis e brinde.")
print("Para isso, preencha os dados a seguir: ")

Nome = input("Nome: ")
valort = float(input("Valor total da compra: "))
Dist = int(input("Distancia da entrega em KM: "))
CE = input("Cupom especial: ")
frete = 40.00
total = 0.00

if valort >= 1000 and CE == "S":
    desconto = valort * 0.20
    valorfinal = valort - desconto
    print("Parabéns! Você ganhou um Mouse pad Gamer de brinde!")
elif valort > 500 and valort < 1000 and CE == "S":
    desconto = valort * 0.10
    valorfinal = valort - desconto
    
if Dist <= 50 and valorfinal >= 200:
    frete = 0.00
    total = valorfinal + frete

else:
    total = valorfinal + frete

print("Nota fiscal: ")
print("Nome", Nome)
print("Valor original", valort)
print("Valor com desconto", valorfinal)
print("Total a pagar", total)

