import random
numero_maquina = random.randint(1, 100)

while True:

    numero_usuario = int(input("Digite o número que você acha que é o verdadeiro: "))

    if numero_usuario == numero_maquina:
        print(f"Parabéns você acertou!! O número era {numero_maquina}")
        continuar = input("Deseja jogar mais uma vez? s/n: ").strip().lower()
        if continuar != "s":
            print("Encerrando...")
            break
        else:
            numero_maquina = random.randint(1, 100)

    elif numero_usuario < numero_maquina:
        print(f"O número {numero_usuario} é menor que o número sorteado")

    elif numero_usuario > numero_maquina:
        print(f"O número {numero_usuario} é maior que o número sorteado")