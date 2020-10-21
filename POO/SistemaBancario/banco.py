class Banco:
    def __init__(self):
        self.agencia = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def adicionar_cliente(self, cliente):
        self.clientes.append(cliente)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def autenticar_cliente(self, cliente):
        if cliente not in self.clientes:
            print("Cliente não encontrado.\n")
            return False
        elif cliente.conta not in self.contas:
            print("Conta do cliente não encontrada.\n")
            return False
        if cliente.conta._agencia not in self.agencia:
            print("Agência da conta não encontrada.\n")
            return False

        return True

    def listar_clientes(self):
        for cliente in self.clientes:
            print(cliente)
