def calculador_media():
    total_notas = 0
    quantidade_nota = 0
    
    while True:
        nota = float(input("Digite suas notas, uma de cada vez (Digite -1 para parar): "))
        if nota == -1:
            break
        total_notas += nota
        quantidade_nota += 1
    return total_notas / quantidade_nota

print(f"Média: {calculador_media()}")
