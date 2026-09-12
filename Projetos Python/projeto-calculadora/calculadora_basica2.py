import math

def calculadora(conta):
    operadores = ["+", "-", "*", "/", "^", "raiz"]
    operador = []
    conta = conta.replace(" ","")
    conta = conta.replace(",",".")
    
    for i in conta:
        if i in operadores:
            operador = i

    numeros = conta.split(i)
    
    numeros[0] = int(numeros[0])
    numeros[1] = int(numeros[1])

    if "+" == operador:
        total = numeros[0] + numeros[1]
    elif "-" == operador:
        total = numeros[0] - numeros[1]
    elif "*" == operador:
        total = numeros[0] * numeros[1]
    elif "/" == operador:
        if numeros[1] == 0:
            return "Não é possível dividir por zero"
        else:
            total = numeros[0] / numeros[1]
    elif operador == "^":
            total = numeros[0] ** numeros[1]
    elif operador == "raiz":
        if numeros[1] != "1 2 3 4 5 6 7 8 9 0":
            return None
        total = math.sqrt(numeros[0])

    return total, numeros[0], numeros[1], operador

while True:
    conta = str(input("Digite aqui sua conta: "))
    tudo = calculadora(conta)
    if tudo == "Não é possível dividir por zero":
        print(tudo)
    else:
        print(f"Resultado: {tudo[1]} {tudo[3]} {tudo[2]} = {round(tudo[0], 2)}")
    
    continuar = input("\nDeseja calcular outro número? (s/n): ").strip().lower()
    if continuar != "s":
        print("Encerrando calculadora...")
        break
    else:
        continue