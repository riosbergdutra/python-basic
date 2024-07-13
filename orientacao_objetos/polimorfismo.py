# Classe base (superclasse) Animal
class Animal:
    def __init__(self, nome):
        self.nome = nome
    
    def fazer_som(self):
        pass  # Método a ser sobrescrito pelas subclasses

# Subclasses de Animal com implementações específicas

class Cachorro(Animal):
    def fazer_som(self):
        return "Au au!"

class Gato(Animal):
    def fazer_som(self):
        return "Miau!"

class Vaca(Animal):
    def fazer_som(self):
        return "Muu!"

# Função para fazer um animal emitir som
def emitir_som(animal):
    return animal.fazer_som()

# Exemplo de uso do polimorfismo
animais = [Cachorro("Rex"), Gato("Garfield"), Vaca("Mimosa")]

for animal in animais:
    print(f"{animal.nome} faz: {emitir_som(animal)}")
