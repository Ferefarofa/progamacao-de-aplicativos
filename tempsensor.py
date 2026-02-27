temp = float(input("Qual a temperatura?: "))
if temp >= 80:
    print("PERIGO! Desligando servidor por superaquecimento!")
elif temp >= 50:
    print("Alerta: Ventoinhas ligadas no máximo!")
elif temp < 50:
    print("Sistemas funcionando normalmente.")