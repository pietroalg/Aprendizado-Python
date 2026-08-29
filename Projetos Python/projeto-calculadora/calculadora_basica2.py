# Remover o print das funções
# Remover todas a funções desnecessarias de soma inteiro

def soma_decimal(n1, n2):
    resultado = n1 + n2
    return resultado

def subtracao_decimal(n1, n2):
    resultado = n1 - n2
    return resultado

def divisao_decimal(n1, n2):
    if n2 == 0:
        resultado = "Não é possível dividir por zero"
    else:
        resultado = n1 / n2
        resultado = round(resultado, 2)
    return resultado

def multiplicacao_decimal(n1, n2):
    resultado = n1 * n2
    return resultado

while True:
    
        print("Olá como você deseja calcular?")
        print("+) Somar","-) Subtrair","/) Dividir","*) Multiplicar", "x) Sair")
        
        escolha_calculo = input("")
    
        if escolha_calculo == "+":
            n1 = float(input("Primeiro número que deseja somar: "))
            n2 = float(input("Segundo número que deseja somar: "))
            soma_decimal = soma_decimal(n1, n2)
            print(f"{n1} + {n2} = {soma_decimal}")
    
        elif escolha_calculo == "-":
            n1 = float(input("Primeiro número que deseja subtrair: "))
            n2 = float(input("Segundo número que deseja subtrair: "))
            sub_decimal = subtracao_decimal(n1, n2)
            print(f"{n1} - {n2} = {sub_decimal}")
    
        elif escolha_calculo == "/":
            n1 = float(input("Primeiro número que deseja dividir: "))
            n2 = float(input("Segundo número que deseja dividir: "))
            div_decimal = divisao_decimal(n1, n2)
            print(f"{n1} / {n2} = {div_decimal}")

        elif escolha_calculo == "*":
            n1 = float(input("Primeiro número que deseja multiplicar: "))
            n2 = float(input("Segundo número que deseja multiplicar: "))
            multi_decimal = multiplicacao_decimal(n1, n2)
            print(f"{n1} * {n2} = {multi_decimal}")

        elif escolha_calculo == "x" or escolha_calculo == "X":
            print("Encerrando calculadora...")
            break
    
        continuar = input("\nDeseja calcular outro número? (s/n): ").strip().lower()
        if continuar != "s":
            print("Encerrando calculadora...")
            break
        else:
            continue