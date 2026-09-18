def calcular_temp(c):
    fahrenheit = c * 9/5 + 32
    return fahrenheit

c = int(input("Digite sua temperatura em Celsius: "))
print(f"Temperatura em Fahrenheit: {calcular_temp(c)}")