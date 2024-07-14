# Definição da função mensagem que recebe um nome e retorna uma saudação simples
def mensagem(nome):
    print("executando mensagem")
    return f"Oi {nome}"

# Definição da função mensagem_longa que recebe um nome e retorna uma saudação mais longa
def mensagem_longa(nome):
    print("executando mensagem longa")
    return f"Olá tudo bem com você {nome}?"

# Função executar recebe uma função (funcao) e um nome como parâmetros,
# imprime uma mensagem indicando a execução e chama a função com o nome,
# retornando o resultado da função
def executar(funcao, nome):
    print("executando executar")
    return funcao(nome)

# Exemplos de execução das funções
print(executar(mensagem, "Joao"))
print(executar(mensagem_longa, "Joao"))
