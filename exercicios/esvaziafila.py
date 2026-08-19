fila = ["Felipe", "Isa", "Jao", "Duda", "Mario", "Vaca"]
while fila[0] != "Vaca":
    fila.pop(0)
    print("Fila: ", fila)
if fila[0] == "Vaca":
    print("Vaca atendida.")