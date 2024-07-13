# Criando um dicionário inicial
meu_dicionario = {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Método clear() - remove todos os elementos do dicionário
meu_dicionario.clear()
print("Após clear():", meu_dicionario)  # Saída: {}

# Adicionando elementos novamente para os métodos restantes
meu_dicionario['nome'] = 'João'
meu_dicionario['idade'] = 30
meu_dicionario['cidade'] = 'São Paulo'

# Método copy() - retorna uma cópia superficial do dicionário
copia_dicionario = meu_dicionario.copy()
print("Cópia do dicionário:", copia_dicionario)  # Saída: {'nome': 'João', 'idade': 30, 'cidade': 'São Paulo'}

# Método get(key[, default]) - retorna o valor associado à chave ou um valor padrão se a chave não existir
print("Valor de 'nome':", meu_dicionario.get('nome'))  # Saída: 'João'
print("Valor de 'email':", meu_dicionario.get('email', 'Nenhum valor encontrado'))  # Saída: 'Nenhum valor encontrado'

# Método items() - retorna uma visualização de pares chave-valor do dicionário
print("items():", meu_dicionario.items())  # Saída: dict_items([('nome', 'João'), ('idade', 30), ('cidade', 'São Paulo')])

# Método keys() - retorna uma visualização das chaves do dicionário
print("keys():", meu_dicionario.keys())  # Saída: dict_keys(['nome', 'idade', 'cidade'])

# Método values() - retorna uma visualização dos valores do dicionário
print("values():", meu_dicionario.values())  # Saída: dict_values(['João', 30, 'São Paulo'])

# Método pop(key[, default]) - remove e retorna o valor associado à chave especificada
valor_removido = meu_dicionario.pop('idade')
print("Valor removido:", valor_removido)  # Saída: 30
print("Após pop('idade'):", meu_dicionario)  # Saída: {'nome': 'João', 'cidade': 'São Paulo'}

# Método popitem() - remove e retorna o último par chave-valor adicionado ao dicionário
par_removido = meu_dicionario.popitem()
print("Par removido:", par_removido)  # Saída: ('cidade', 'São Paulo')
print("Após popitem():", meu_dicionario)  # Saída: {'nome': 'João'}

# Método update(other_dict) - atualiza o dicionário com elementos de outro dicionário
outro_dicionario = {'cidade': 'Rio de Janeiro', 'profissao': 'Engenheiro'}
meu_dicionario.update(outro_dicionario)
print("Após update():", meu_dicionario)  # Saída: {'nome': 'João', 'cidade': 'Rio de Janeiro', 'profissao': 'Engenheiro'}

# Método setdefault(key[, default]) - retorna o valor associado à chave, se existir; senão, insere a chave com o valor padrão e retorna o valor padrão
print("setdefault('email'):", meu_dicionario.setdefault('email', 'Nenhum email cadastrado'))  # Saída: 'Nenhum email cadastrado'
print("Após setdefault():", meu_dicionario)  # Saída: {'nome': 'João', 'cidade': 'Rio de Janeiro', 'profissao': 'Engenheiro', 'email': 'Nenhum email cadastrado'}

# Método fromkeys(seq[, value]) - cria um novo dicionário com chaves a partir de uma sequência e valores opcionais
sequencia = ['a', 'b', 'c']
novo_dicionario = dict.fromkeys(sequencia, 0)
print("fromkeys():", novo_dicionario)  # Saída: {'a': 0, 'b': 0, 'c': 0}

# Método __contains__(key) - verifica se a chave especificada existe no dicionário
print("'nome' in meu_dicionario:", 'nome' in meu_dicionario)  # Saída: True
print("'telefone' in meu_dicionario:", 'telefone' in meu_dicionario)  # Saída: False