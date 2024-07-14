def meu_gerador(numeros: list[int]):
    for numero in numeros:
        yield numero * 2

# Utilizando o gerador em um loop for
for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)

# os geradores são uma poderosa ferramenta em Python para trabalhar com sequências de dados de forma eficiente e flexível, especialmente em situações onde a performance e o uso de memória são preocupações.