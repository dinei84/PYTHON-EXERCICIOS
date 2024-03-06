numero = 30

while numero > 0:
    if numero % 4 == 0:
        print(f"[{numero}]", end=" ")
    else:
        print(numero, end=" ")
    numero -= 1

print("\nFim da contagem regressiva!")
