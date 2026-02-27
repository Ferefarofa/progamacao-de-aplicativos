print("Para saber se foi aprovado preencha os dados a seguir: ")
print(" ")

media = float(input("Qual a sua média ?: "))
pres = int(input("Qual a sua porcentagem de frequencia ?: "))

if media >= 7.0 and pres >= 75:
    print("Parabéns! Você foi aprovado! ")
else:
    print("Reprovado. Verifique sua nota ou frequência. ")
    