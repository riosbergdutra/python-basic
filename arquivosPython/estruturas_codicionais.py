MAIOR_IDADE = 18    #Constante é colocado tudo maiusculo 
IDADE_ESPECIAL = 17

idade = int(input("informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH")

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")   # colocando else



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL: # adicionando elif semelhante ao else if
    print("pode fazer aulas teóricas, mas não pode fazer aulas praticas.")
else:
    print("Ainda não pode tirar a CNH")   # colocando else


