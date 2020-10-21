from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo=0):
        self._agencia = agencia
        self._numero_conta = numero_conta
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser int ou float.")

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser int ou float.")

        self.saldo += valor
        self.detalha_conta()

    @abstractmethod
    def sacar(self, valor):
        pass

    def detalha_conta(self):
        print(f'Agência: {self._agencia}')
        print(f'Número da conta: {self._numero_conta}')
        print(f'Saldo: R${self.saldo:.2f}\n')


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo=0, limite=0):
        super().__init__(agencia, numero_conta, saldo)
        self._limite = limite

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser int ou float.")

        self._saldo = valor

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser int ou float.")

        self._limite = valor

    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser int ou float.")

        if self.saldo + self.limite - valor < 0:
            print("Saldo Insuficiente. Limite vai ser ultrapassado.")
        else:
            self.saldo -= valor
            self.detalha_conta()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor precisa ser int ou float.")
        if self.saldo - valor < 0:
            print("Não há saldo suficiente na conta.")
        else:
            self.saldo -= valor
            self.detalha_conta()
