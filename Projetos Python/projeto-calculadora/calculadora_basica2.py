# Remover o print das funções
# Remover todas a funções desnecessarias de soma inteiro
def calculadora(conta):
    operadores = ["+", "-", "*", "/", "^"]

    conta = conta.replace(" ","")
    conta = conta.replace(",",".")
    for i in conta:
        if i == operadores:
            operador = i
            break

    numeros = conta.split(operador)
    
    numeros[0] = float(numeros[0])
    numeros[1] = float(numeros[1])

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

    return total, numeros[0], numeros[1], operador

while True:
    conta = str(input("Digite aqui sua conta: "))
    tudo = calculadora(conta)
    if tudo == "Não é possível dividir por zero":
        print(tudo)
    else:
        print(f"Resultado: {tudo[1]} {tudo[3]} {tudo[2]}= {round(tudo[0], 2)}")
    
    continuar = input("\nDeseja calcular outro número? (s/n): ").strip().lower()
    if continuar != "s":
        print("Encerrando calculadora...")
        break
    else:
        continue