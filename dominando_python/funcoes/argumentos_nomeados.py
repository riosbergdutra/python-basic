def salvar_carro(marca, modelo, ano, placa):
    # caso alguem altere a ordem do parametro não terá problemas pois o argumento foi definido corretamente com argumento nomeado
    # salva o carro no banco de dados...
    print(f"Carro inserido no com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Palio", "Fiat", 1999, "ABC-1234") # capaz de errar caso não nomeie corretamente
# salvar_carro(marca="Fiat", modelo="Palio", ano="1999", placa="ABC-1234") argumento nomeado