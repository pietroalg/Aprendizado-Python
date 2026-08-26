def soma(n1, n2):
    resultado = n1 + n2
    print(f"{n1} + {n2} = {resultado}")
def subtracao(n1, n2):
    resultado = n1 - n2
    print(f"{n1} - {n2} = {resultado}")
def divisao(n1, n2):
    resultado = n1 / n2
    print(f"{n1} / {n2} = {resultado}")
def multiplicacao(n1, n2):
    resultado = n1 * n2
    print(f"{n1} * {n2} = {resultado}")

lista_prompt = ["A", "a", "B", "b", "C", "c", "D", "d"]


while True:
    print("Calculadora Básica")

    n1 = int(input("Digite o primeiro número que você deseja calcular: "))
    n2 = int(input("Digite o segundo número que você deseja calcular: "))

    print("A) Somar", "B) Subtrair", "C) Dividir", "D) Multiplicar")
    decisao_calculo = input("Qual das opções acima você quer seguir?: ")

    if decisao_calculo in lista_prompt:
        pass
    else:
        print("Valor inválido,} tente novamente...")
        continue

    if decisao_calculo == "A" or decisao_calculo == "a":
        soma(n1, n2)
        pass

    if decisao_calculo == "B" or decisao_calculo == "b":
        subtracao(n1, n2)
        pass

    if decisao_calculo == "C" or decisao_calculo == "c":
        divisao(n1, n2)
        pass

    if decisao_calculo == "D" or decisao_calculo == "d":
        multiplicacao(n1, n2)
        pass
    continuar = input("\nDeseja calcular outro número? (s/n): ").strip().lower()
    if continuar != "s":
        print("Encerrando calculadora...")
        break