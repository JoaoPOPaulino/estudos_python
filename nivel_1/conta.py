class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    @property
    def titular(self):
        return self._titular
    @titular.setter
    def titular(self, novo_titular):
        if not novo_titular:
            raise ValueError("O titular da conta não pode ser vazio.")
        self._titular = novo_titular

    @property
    def saldo(self):
        return self._saldo
    @saldo.setter
    def saldo(self, novo_saldo):
        if novo_saldo < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = novo_saldo

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do depósito deve ser maior que zero.")
        self.saldo += valor

    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente para o saque.")
        self.saldo -= valor

    def tem_saldo(self):
        if self.saldo <= 0:
            return False
        return True

    def __str__(self):
        return f"ContaBancaria(titular='{self.titular}', saldo={self.saldo})"

conta1 = ContaBancaria("João", 1000)
conta2 = ContaBancaria("Maria", 2500)

print(conta1)
print(conta2)

conta1.depositar(500)
print(conta1.saldo)
# 1500

conta2.sacar(400)
print(conta2.saldo)
# 2100

print(conta1.tem_saldo())
# True

conta1.sacar(2000)
# ValueError
conta = ContaBancaria("João", 1000)

print(conta)