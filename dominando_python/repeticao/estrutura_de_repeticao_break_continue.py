while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        print("fim da repeticao")
        break

    print(numero)

for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero)