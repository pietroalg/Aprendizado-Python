total_notas = 0
quantidade_nota = 0

while True:
    nota = float(input("Digite suas notas, uma de cada vez: "))
    if nota == -1:
        break
    total_notas += nota
    quantidade_nota += 1


print(f"Sua média foi: {total_notas / quantidade_nota}")