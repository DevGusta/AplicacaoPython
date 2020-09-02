"""
Este validador de CPF foi feito como aplicação de conteúdos aprendidos em python
"""

print("Validador de CPF!!")

while True:
    cpf_do_usuario = input('Digite um CPF sem "." e sem "-": ')

    # Verificando se o CPF digitado é valor númerico es e foi digitado mais ou menos números de CPF
    if cpf_do_usuario.isnumeric() and len(cpf_do_usuario) == 11:
        cpf = cpf_do_usuario[:-2]   # Retira os 2 últimos digitos do CPF digitado
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

        if cpf == cpf_do_usuario:  # Verificando se o CPF é válido
            print("CPF válido.")
        else:
            print("CPF inválido.")
    else:
        print('Você digitou o CPF incorretamente. Tente novamente.')
