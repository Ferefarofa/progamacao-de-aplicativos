print("Checagem de umidade, insira os dados.")
temperatura = float(input("Qual a temperatura atual?: "))
if temperatura <= 30.0:
    print("Clima estável.")
elif temperatura > 30.0:
    print("Alerta de Calor!")
    print(" ")
    umidade = float(input("Qual a umidade?: "))
    if umidade < 40.0:
        print("Ligar irrigação. ")
    else:
        print("Ligar ventiladores")