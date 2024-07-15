from datetime import datetime

# Obter a data e hora atuais
data_hora_atual = datetime.now()

# String de data e hora a ser convertida para um objeto datetime
data_hora_str = "2023-10-20 10:20"

# Máscaras de formatação para exibição da data e hora
mascara_ptbr = "%d/%m/%Y %H:%M"
mascara_en = "%Y-%m-%d %H:%M"

# Exibir a data e hora atuais formatadas de acordo com a máscara brasileira (dia/mês/ano hora:minuto)
print(data_hora_atual.strftime(mascara_ptbr))

# Converter a string de data e hora para um objeto datetime usando a máscara de entrada
data_convertida = datetime.strptime(data_hora_str, mascara_en)

# Exibir a data e hora convertidas e o tipo do objeto resultante
print(data_convertida)
print(type(data_convertida))
