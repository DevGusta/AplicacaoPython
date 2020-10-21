from banco import Banco
from clientes import Cliente
from contas import ContaPoupanca, ContaCorrente

bank = Banco()

cliente1 = Cliente('Gustavo', 18)
cliente2 = Cliente('Maria', 32)
cliente3 = Cliente('Rose', 27)

conta1 = ContaCorrente(2222, 12345, 500)
conta2 = ContaPoupanca(3333, 23456)
conta3 = ContaCorrente(4444, 34567, 100)

cliente1.adicionar_conta(conta1)
cliente2.adicionar_conta(conta2)
cliente3.adicionar_conta(conta3)

bank.adicionar_cliente(cliente1)
bank.adicionar_conta(conta1)

bank.adicionar_cliente(cliente2)
bank.adicionar_conta(conta2)

if bank.autenticar_cliente(cliente1):
    cliente1.conta.sacar(200)

if bank.autenticar_cliente(cliente2):
    cliente2.conta.depositar(150.90)

if bank.autenticar_cliente(cliente3):
    cliente3.conta.depositar(250)

cliente3.conta.detalha_conta()
