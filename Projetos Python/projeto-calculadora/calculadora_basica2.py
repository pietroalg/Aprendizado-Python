# Remover o print das funções
# Remover todas a funções desnecessarias de soma inteiro

def soma_decimal(n1, n2):
    resultado = n1 + n2
    return resultado

def subtracao_decimal(n1, n2):
    resultado = n1 - n2
    return resultado

def divisao_decimal(n1, n2):
    resultado = n1 / n2
    return resultado

def multiplicacao_decimal(n1, n2):
    resultado = n1 / n2
    return resultado

while True:
    
        print("Olá como você deseja calcular?")
        print("A) Somar","B) Subtrair","C) Dividir","D) Multiplicar")
        
        escolha_calculo = input("")
    
        if escolha_calculo == "A" or escolha_calculo == "a":
            n1 = float(input("Primeiro número que deseja somar: "))
            n2 = float(input("Segundo número que deseja somar: "))
            soma_decimal = soma_decimal(n1, n2)
            print(f"{n1} + {n2} = {soma_decimal:.2f}")
    
        if escolha_calculo == "B" or escolha_calculo == "b":
            n1 = float(input("Primeiro número que deseja subtrair: "))
            n2 = float(input("Segundo número que deseja subtrair: "))
            sub_decimal = subtracao_decimal(n1, n2)
            print(f"{n1} - {n2} = {sub_decimal:.2f}")
    
        if escolha_calculo == "C" or escolha_calculo == "c":
            n1 = float(input("Primeiro número que deseja dividir: "))
            n2 = float(input("Segundo número que deseja dividir: "))
            div_decimal = divisao_decimal(n1, n2)
            print(f"{n1} / {n2} = {div_decimal:.2f}")

    
        if escolha_calculo == "D" or escolha_calculo == "d":
            n1 = float(input("Primeiro número que deseja multiplicar: "))
            n2 = float(input("Segundo número que deseja multiplicar: "))
            multi_decimal = multiplicacao_decimal(n1, n2)
            print(f"{n1} / {n2} = {multi_decimal:.2f}")
    
        continuar = input("\nDeseja calcular outro número? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando calculadora...")
            break
        else:
            continue