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

<<<<<<< HEAD
while True:
    nota = float(input("Digite suas notas, uma de cada vez (Digite -1 para parar): "))
    if nota == -1:
        break
    total_notas += nota
    quantidade_nota += 1


print(f"Sua média foi: {total_notas / quantidade_nota}")
=======
print(f"Média: {calculador_media()}")
>>>>>>> cfcad819f056da6f80516dbde89b13d041894c52
