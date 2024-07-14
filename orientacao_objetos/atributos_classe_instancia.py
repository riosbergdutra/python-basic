class Estudante:
    escola = "DIO" # Variável de classe

    def __init__(self, nome, matricula):
        self.nome = nome # Variável de instância
        self.matricula = matricula # Variável de instância

    def __str__(self) -> str:
        return f"{self.nome} - {self.matricula} - {self.escola}"


def mostrar_valores(*objs):
    for obj in objs:
        print(obj)


aluno_1 = Estudante("Guilherme", 1)
aluno_2 = Estudante("Giovanna", 2)
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = "Python" # Modificação da variável de classe
aluno_3 = Estudante("Chappie", 3)
mostrar_valores(aluno_1, aluno_2, aluno_3)