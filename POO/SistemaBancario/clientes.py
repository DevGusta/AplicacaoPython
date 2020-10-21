class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def adicionar_conta(self, conta):
        self.conta = conta
