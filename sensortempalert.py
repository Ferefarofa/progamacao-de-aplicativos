temps = [28.5, 31.0, 29.8, 33.5, 27.0, 35.2, 30.0]
perg = ""
while perg != "fim":
    perg = input("Insira tempreatura, se não quiser digite (fim): ")
    if perg != "fim":
        temps.append(perg)
for temp in temps:
    if temp > 30:
        print(f"\nALERTA: Temperatura Crítica! ({temp}°C)")
    else:
        print(f"Temperatura Normal. ({temp}°C)")
