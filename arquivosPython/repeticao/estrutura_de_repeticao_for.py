texto = input("")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()
    print("Execute no final do laço")

# exemplo de range
for numero in range(0, 51, 5):
    print(numero, end="")