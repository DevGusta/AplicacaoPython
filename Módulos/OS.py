"""
Programa para encontrar um arquivo no seu sistema utilizando o módulo OS e retornar as informações:
Caminho completo, nome, extensão e tamanho do arquivo.
"""

import os

caminho_procura = input('Digite um caminho:')
termo_procura = input('Digite o arquivo que procura:')


def formata_tamanho(tamanho):
    base = 1024
    kilo = base
    mega = base ** 2
    giga = base ** 3
    tera = base ** 4
    peta = base ** 5

    if tamanho < kilo:
        texto = 'B'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'K'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'M'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'G'
    elif tamanho < peta:
        tamanho /= tera
        texto = 'T'
    else:
        tamanho /= peta
        texto = 'P'

    tamanho = round(tamanho, 2)

    return f'{tamanho} {texto}'.replace('.', ',')


conta = 0
for raiz, diretorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                conta += 1
                caminho_completo = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminho_completo)

                print()
                print('Encontrei o arquivo: ', arquivo)
                print('Caminho: ', caminho_completo)
                print('Nome: ', nome_arquivo)
                print('Extensão: ', ext_arquivo)
                print('Tamanho: ', tamanho)
                print('Tamanho formatado: ', formata_tamanho(tamanho))

            except PermissionError as e:
                print('Sem permissões.')
            except FileExistsError as e:
                print('Não exite.')
            except Exception as e:
                print('Erro desconhecido.')

print(f'{conta} arquivos encontrados.')
