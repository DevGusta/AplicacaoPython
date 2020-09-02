"""
Adaptando o Validador de CPF para Gerador de CPF
"""

from random import randint
numero = str(randint(100000000, 999999999))

cpf = numero   # Cria 8 números aleatório
soma1 = 0  # Soma dos resultados da multiplicação
soma2 = 0

regresso = 10  # Contador regressivo
for i in range(9):  # Contador dos 8 números do CPF sem os dígitos
    conta = int(cpf[i]) * regresso
    soma1 += conta
    regresso -= 1

c_digito1 = 11 - (soma1 % 11)  # Cálculo do primeiro dígito
if c_digito1 > 9:
    digito1 = 0
else:
    digito1 = c_digito1
cpf += str(digito1)  # Adição do primeiro dígito ao CPF

regresso = 11
for i in range(10):  # Contador dos 8 números do CPF e do primeiro dígito
    conta = int(cpf[i]) * regresso
    soma2 += conta
    regresso -= 1

c_digito2 = 11 - (soma2 % 11)   # Cálculo do segundo dígito
if c_digito2 > 9:
    digito2 = 0
else:
    digito2 = c_digito2
cpf += str(digito2)  # Adição do segundo digito ao CPF

print(cpf)
