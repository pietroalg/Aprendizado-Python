import random
numero_maquina = random.randint(1, 100)

def comparador_numeros(numero_usuario, numero_maquina):

    if numero_usuario == numero_maquina:
        resultado = f"Parabéns você acertou!! O número era {numero_maquina}"
        numero_maquina = random.randint(1, 100)
        
    elif numero_usuario < numero_maquina:
        resultado = f"O número {numero_usuario} é menor que o número sorteado"
        
    elif numero_usuario > numero_maquina:
        resultado = f"O número {numero_usuario} é maior que o número sorteado"

    return resultado

while True:

    numero_usuario = int(input("Digite o número que você acha que é o verdadeiro (Digite 0 caso deseja sair): "))
    print(comparador_numeros(numero_usuario, numero_maquina))