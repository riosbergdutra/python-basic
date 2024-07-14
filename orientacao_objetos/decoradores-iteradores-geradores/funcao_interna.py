# Definição da função principal
def principal():
    print("executando a funcao principal")

    # Função interna dentro de principal
    def funcao_interna():
        print("executando a funcao interna")

    # Outra função interna dentro de principal
    def funcao_2():
        print("executando a funcao 2")

    # Chamada das funções internas
    funcao_interna()
    funcao_2()

# Executa a função principal
principal()
