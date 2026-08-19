vida = 100
def sofrer_dano(vida, dano): 
    vida -= dano
    print(f"Você tem {vida} de vida restante. ")
    return(vida)
while vida > 0:
    valor_dano = int(input("Quanto de dano o boss deu ?: "))
    vida = sofrer_dano(vida,valor_dano)
print("Game Over...")
