from random import randint


def geraCNPJsemDigitos():
    numero = randint(0, 99999999)
    numero = str(numero)
    numero += '0001'
    return numero


def geradorCNPJ():
    cnpj = geraCNPJsemDigitos()

    cnpj = calculoDigito1(cnpj)
    cnpj = calculoDigito2(cnpj)

    cnpj = formataCNPJ(cnpj)

    return cnpj


def calculoDigito1(cnpj):
    soma = 0
    multiplicador = 5
    for numero in cnpj:
        soma += int(numero) * multiplicador
        multiplicador -= 1
        if multiplicador < 2:
            multiplicador = 9

    formula = 11 - (soma % 11)

    if formula > 9:
        digito1 = 0
    else:
        digito1 = formula

    cnpj += str(digito1)

    return cnpj


def calculoDigito2(cnpj):
    soma = 0
    multiplicador = 6
    for numero in cnpj:
        soma += int(numero) * multiplicador
        multiplicador -= 1
        if multiplicador < 2:
            multiplicador = 9

    formula = 11 - (soma % 11)

    if formula > 9:
        digito2 = 0
    else:
        digito2 = formula

    cnpj += str(digito2)

    return cnpj


def formataCNPJ(cnpj):
    cnpj = f'{cnpj[0:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return cnpj

print(geradorCNPJ())

