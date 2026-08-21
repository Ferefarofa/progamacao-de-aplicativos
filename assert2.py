def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

situacao_aluno(8)
assert situacao_aluno(10) == "Aprovado"
assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"      #É chamado caso de limite pois é a nota mais baixa que ainda leva a aprovação
assert situacao_aluno(5.9) == "Reprovado"   #É chamado caso de limite pois é a nota mais alta que ainda leva a reprova
assert situacao_aluno(4) == "Reprovado"     #Acho bem importante
assert situacao_aluno(0) == "Reprovado"

 # Crie testes para as médias: 6, 5.9, 0 e 10.