def exibir_mensagem():
    print("Olá Mundo!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")

def exibir_mensagem_3(nome):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Guilherne")
exibir_mensagem_3(nome="Matheus") # Neste codigo ocorrerá tudo corretamente

# exibir_mensagem_3() # Neste codigo ocorrerá erro afinal nome não foi definido 

def exibir_mensagem_4(nome="Anonimato"):
    print(f"Seja bem vindo {nome}!")

exibir_mensagem_4() # ocorrerá tudo certo afinal nome foi definido no parametro da função