class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular  # Atributo protegido
        self._saldo = saldo  # Atributo protegido inicializado com o saldo inicial

    @property
    def saldo(self):
        """ Retorna o saldo da conta. """
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):
        """ Define um novo saldo para a conta, com validação. """
        if novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            print("Erro: O saldo não pode ser negativo!")

    def depositar(self, valor):
        """ Deposita um valor na conta. """
        self._saldo += valor

    def sacar(self, valor):
        """ Saca um valor da conta, com validação de saldo suficiente. """
        if valor <= self._saldo:
            self._saldo -= valor
        else:
            print("Erro: Saldo insuficiente!")

# Exemplo de uso da classe ContaBancaria
conta = ContaBancaria("João", 1000)  # Cria uma conta com saldo inicial de 1000
print(f"Saldo inicial: {conta.saldo}")  # Saída: Saldo inicial: 1000

conta.depositar(500)  # Deposita 500 na conta
print(f"Saldo após depósito: {conta.saldo}")  # Saída: Saldo após depósito: 1500

conta.sacar(200)  # Saca 200 da conta
print(f"Saldo após saque: {conta.saldo}")  # Saída: Saldo após saque: 1300

conta.saldo = 3000  # Define um novo saldo usando o setter
print(f"Novo saldo: {conta.saldo}")  # Saída: Novo saldo: 3000

conta.saldo = -500  # Tenta definir um saldo negativo (irá gerar um erro)
print(f"Saldo após tentativa de saldo negativo: {conta.saldo}")  # Saída: Erro: O saldo não pode ser negativo!
                                                                  #        Saldo após tentativa de saldo negativo: 3000
