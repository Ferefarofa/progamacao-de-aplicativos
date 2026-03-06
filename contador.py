numero = int(input("Qual o número da garrafa que está passando pela esteira ?: "))
if numero % 100 == 0:
    print("QUALIDADE: Retirar amostra para teste. ")
if numero % 500 == 0:
    print("HORA DA LIMPEZA: Parar máquina imediatamente! ")
else:
    print(f"Produção em dia. Garrafa número {numero} processada")