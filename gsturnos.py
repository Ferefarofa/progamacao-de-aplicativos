id = int(input("Qual o seu ID ?: "))
temperatura = float(input("Qual a temperatura da máquina que você opera?: "))
tempo = int(input("Qual o tempo de uso ?: "))

if (id % 3 == 0) and (temperatura > 40 or tempo > 8):
    print(f"Funcionário {id}, você foi escalado para a manutenção preventiva hoje.")
else:
    print(f"Funcionário {id}, sua máquina opera dentro dos padrões normais.")