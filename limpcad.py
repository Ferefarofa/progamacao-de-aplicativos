usuarios = ["admin", "convidado", "suporte", "teste"]
print(usuarios)
usuarios.remove("teste")
del usuarios[0]
print(f"A lista após as exclusões agora é: {usuarios}")