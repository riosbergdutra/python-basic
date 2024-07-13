# Definindo a primeira classe base
class ClasseA:
    def metodo_a(self):
        return "Método da ClasseA"

# Definindo a segunda classe base
class ClasseB:
    def metodo_b(self):
        return "Método da ClasseB"

# Definindo a terceira classe base
class ClasseC:
    def metodo_c(self):
        return "Método da ClasseC"

# Definindo a classe derivada que herda de ClasseA, ClasseB, e ClasseC
class ClasseD(ClasseA, ClasseB, ClasseC):
    def metodo_d(self):
        return "Método da ClasseD"

# Criando uma instância da ClasseD
objeto_d = ClasseD()

# Testando os métodos herdados de ClasseA, ClasseB e ClasseC
print(objeto_d.metodo_a())  # Saída: Método da ClasseA
print(objeto_d.metodo_b())  # Saída: Método da ClasseB
print(objeto_d.metodo_c())  # Saída: Método da ClasseC

# Testando o método definido em ClasseD
print(objeto_d.metodo_d())  # Saída: Método da ClasseD
