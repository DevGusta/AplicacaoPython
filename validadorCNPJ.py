def validaCNPJ(cnpj):
    cnpj = removeCaracteres(cnpj)

    novocnpj = removeDigitos(cnpj)

    if eh_sequencia(novocnpj):
        return "Inválido."

    novocnpj = calculoDigito1(novocnpj)
    novocnpj = calculoDigito2(novocnpj)

    if novocnpj == cnpj:
        return 'Válido.'
    else:
        return 'Inválido.'


def removeCaracteres(cnpj):
    cnpj = cnpj.replace('.', '')
    cnpj = cnpj.replace('/', '')
    cnpj = cnpj.replace('-', '')
    return cnpj


def removeDigitos(cnpj):
    cnpj = cnpj[0:-2]
    return cnpj


def eh_sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)

    if sequencia == cnpj:
        return True
    else:
        return False


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


cnpjUsuario = input("Digite seu CNPJ: ")
print(validaCNPJ(cnpjUsuario))
