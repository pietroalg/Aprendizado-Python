import random
numero_maquina = random.randint(1, 100)

def comparador_numeros(numero_usuario_int, numero_maquina_int):

    if numero_usuario_int == numero_maquina_int:
        resultado = f"Parabéns você acertou!! O número era {numero_maquina}"
        numero_maquina_int = random.randint(1, 100)
        
    elif numero_usuario_int < numero_maquina_int:
        resultado = f"O número {numero_usuario} é menor que o número sorteado"
        
    elif numero_usuario_int > numero_maquina_int:
        resultado = f"O número {numero_usuario} é maior que o número sorteado"

    return resultado, numero_maquina_int 

while True:

    numero_usuario = int(input("Digite o número que você acha que é o verdadeiro (Digite 0 caso deseja sair): "))
    lista_ret = comparador_numeros(numero_usuario, numero_maquina)
    numero_maquina = lista_ret[1]
    print(lista_ret[0])