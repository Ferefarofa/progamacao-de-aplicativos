def classificar_temperatura(temperatura):
    if temperatura <= 15:
        return "Frio"
    elif temperatura > 15 and temperatura < 25:
        return "Agradável"
    elif temperatura >= 25:
        return "Quente"


classificar_temperatura(200)
assert classificar_temperatura(10) == "Frio"
assert classificar_temperatura(15) == "Frio"
assert classificar_temperatura(16) == "Agradável"
assert classificar_temperatura(24) == "Agradável"
assert classificar_temperatura(25) == "Quente"
assert classificar_temperatura(30) == "Quente"