temps = [28.5, 31.0, 29.8, 33.5, 27.0, 35.2, 30.0]
perg = ""
while perg != "fim":
    temperatura = float(input("Insira temperatura: "))
    temps.append(temperatura)
    perg = input("Se deseja encerrar o programa digite 'fim': ")
for temp in temps:
    if temp > 30.0:
        print(f"\nALERTA: Temperatura Crítica! ({temp}°C)")
    else:
        print(f"Temperatura Normal. ({temp}°C)")
