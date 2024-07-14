class MeuIterador:
    def __init__(self, numeros: list[int]):
        self.numeros = numeros  # Recebe uma lista de números como argumento
        self.contador = 0  # Inicializa o contador para controlar a posição na lista

    def __iter__(self):
        return self  # Retorna o próprio objeto como iterador

    def __next__(self):
        try:
            numero = self.numeros[self.contador]  # Obtém o número na posição do contador
            self.contador += 1  # Incrementa o contador para apontar para o próximo número
            return numero * 2  # Retorna o número multiplicado por 2
        except IndexError:
            raise StopIteration  # Levanta StopIteration quando todos os elementos foram percorridos

# Usando o iterador MeuIterador com uma lista específica de números
for i in MeuIterador(numeros=[38, 13, 11]):
    print(i)  # Imprime cada número multiplicado por 2





# Exemplo simples de iterador com uma lista
numeros = [1, 2, 3, 4, 5]

# Criando um iterador a partir da lista
iterador = iter(numeros)

# Iterando manualmente com next() e capturando StopIteration
try:
    while True:
        numero = next(iterador)
        print(numero)
except StopIteration:
    pass