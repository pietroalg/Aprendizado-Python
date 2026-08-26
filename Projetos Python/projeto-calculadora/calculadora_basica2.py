def soma_inteiro(n1, n2):
    n1 = int(input("Primeiro número que deseja somar: "))
    n2 = int(input("Segundo número que deseja somar: "))
    resultado = n1 + n2
    print(f"{n1} + {n2} = {resultado}")

def subtracao_inteiro(n1, n2):
    n1 = int(input("Primeiro número que deseja subtrair: "))
    n2 = int(input("Segundo número que deseja subtrair: "))
    resultado = n1 - n2
    print(f"{n1} - {n2} = {resultado}")

def divisao_inteiro(n1, n2):
    n1 = int(input("Primeiro número que deseja dividir: "))
    n2 = int(input("Segundo número que deseja dividir: "))
    resultado = n1 / n2
    print(f"{n1} / {n2} = {resultado}")

def multiplicacao_inteiro(n1, n2):
    n1 = int(input("Primeiro número que deseja multiplicar: "))
    n2 = int(input("Segundo número que deseja multiplicar: "))
    resultado = n1 * n2
    print(f"{n1} * {n2} = {resultado}")

def soma_decimal(n1, n2):
    n1 = float(input("Primeiro número que deseja somar: "))
    n2 = float(input("Segundo número que deseja somar: "))
    resultado = n1 + n2
    print(f"{n1} + {n2} = {resultado:.2f}")

def subtracao_decimal(n1, n2):
    n1 = float(input("Primeiro número que deseja subtrair: "))
    n2 = float(input("Segundo número que deseja subtrair: "))
    resultado = n1 - n2
    print(f"{n1} - {n2} = {resultado:.2f}")

def divisao_decimal(n1, n2):
    n1 = float(input("Primeiro número que deseja dividir: "))
    n2 = float(input("Segundo número que deseja dividir: "))
    resultado = n1 / n2
    print(f"{n1} / {n2} = {resultado:.2f}")

def multiplicacao_decimal(n1, n2):
    n1 = float(input("Primeiro número que deseja multiplicar: "))
    n2 = float(input("Segundo número que deseja multiplicar: "))
    resultado = n1 / n2
    print(f"{n1} / {n2} = {resultado:.2f}")




while True:

    print("Olá, antes de tudo, deseja calcular números inteiros ou números decimais? [int/dec]")
    escolha_numero = input(" ")

    if escolha_numero == "int":
        print("Olá como você deseja calcular?")
        print("A) Somar", "B) Subtrair", "C) Dividir", "D) Multiplicar")
        
        escolha_calculo = input(" ")
    
        if escolha_calculo == "A" or escolha_calculo == "a":
            soma_inteiro(n1, n2)
    
        if escolha_calculo == "B" or escolha_calculo == "b":
            subtracao_inteiro(n1, n2)
    
        if escolha_calculo == "C" or escolha_calculo == "c":
            divisao_inteiro(n1, n2)
    
        if escolha_calculo == "D" or escolha_calculo == "d":
            multiplicacao_inteiro(n1, n2)
    
        continuar = input("\nDeseja calcular outro número? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando calculadora...")
            break
        else:
            continue
    else:
        print("Olá como você deseja calcular?")
        print("A) Somar", "B) Subtrair", "C) Dividir", "D) Multiplicar")
        
        escolha_calculo = input(" ")
    
        if escolha_calculo == "A" or escolha_calculo == "a":
            soma_decimal(n1, n2)
    
        if escolha_calculo == "B" or escolha_calculo == "b":
            subtracao_decimal(n1, n2)
    
        if escolha_calculo == "C" or escolha_calculo == "c":
            divisao_decimal(n1, n2)
    
        if escolha_calculo == "D" or escolha_calculo == "d":
            multiplicacao_decimal(n1, n2)
    
        continuar = input("\nDeseja calcular outro número? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando calculadora...")
            break
        else:
            continue