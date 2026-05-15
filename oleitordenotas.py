import json

# abre e lê o arquivo JSON
with open("notas.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

# pega as notas
matematica = dados["matematica"]
portugues = dados["portugues"]

# soma as notas
soma = matematica + portugues

# mostra o resultado
print("Soma das notas:", soma)