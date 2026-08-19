print("Você ira lutar contra o vilão!!! Preencha os dadps a seguir para saber o resultado da luta: ")
print(" ")

ataque = int(input("Quantos pontos de ataque você tem ?: "))
defesa = int(input("Quantos pontos de defesa o vilão tem ?: "))
result = ataque - defesa

if result <= 0:
    print("O vilão bloqueou o ataque! Dano: 0")
elif result > 0:
    print("Ataque crítico! Você causou dano ao vilão de ", result)
     