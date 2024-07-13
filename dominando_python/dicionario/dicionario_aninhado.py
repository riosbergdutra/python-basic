meu_dicionario = {}

meu_dicionario['informacoes'] = {
    'nome': 'João',
    'idade': 30,
    'cidade': 'São Paulo'
}

meu_dicionario['outras_informacoes'] = {
    'profissao': 'Engenheiro',
    'telefone': '123456789'
}

print(meu_dicionario)
# Saída:
# {
#   'informacoes': {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'},
#   'outras_informacoes': {'profissao': 'Engenheiro', 'telefone': '123456789'}
# }

# Acessando valores do dicionário aninhado
print(meu_dicionario['informacoes']['nome'])  # Saída: 'João'
print(meu_dicionario['outras_informacoes']['profissao'])  # Saída: 
