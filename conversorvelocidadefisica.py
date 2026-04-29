def converter_km_para_ms(velocidade):
    if velocidade > 80:
        ms = kmh / 3.6
        print(f"Atenção, reduza a velocidade, você está a {ms} metros por segundo!!!")
    else:
        print("Velocidade dentro dos padrões. ")
kmh = int(input("Qual a sua velocidade em KM/H ?: "))
converter_km_para_ms(kmh)

    