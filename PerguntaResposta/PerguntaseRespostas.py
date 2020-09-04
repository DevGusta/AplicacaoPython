"""
Criação de um sistema de perguntas e respostas utilizando dicionários.
"""


perguntas = {  # Dicionário com as perguntas, alternativas de respostas e a resposta correta.
    'Pergunta 1': {
        'pergunta': 'Quanto é 2 + 2?',
        'respostas': {'a': '1', 'b': '4', 'c': '5'},
        'reposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3 * 2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'reposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 5 * 2?',
        'respostas': {'a': '4', 'b': '10', 'c': '6'},
        'reposta_certa': 'b',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 6 / 2?',
        'respostas': {'a': '3', 'b': '5', 'c': '2'},
        'reposta_certa': 'a',
    },
    'Pergunta 5': {
        'pergunta': 'Quanto é 1 - 2?',
        'respostas': {'a': '0', 'b': '1', 'c': '-1'},
        'reposta_certa': 'c',
    },
}
respostas_certas = 0  # Variável para acumular as respostas corretas.
for pk, pv in perguntas.items():  # Laço para as perguntas.
    print(f'{pk}: {pv["pergunta"]}')

    for rk, rv in pv['respostas']. items():  # Laço para as alternativas.
        print(f'[{rk}]: {rv}')

    resposta_usuario = input("Digite sua resposta:")  # Resposta do usuário.
    if resposta_usuario == pv['reposta_certa']:
        print('Você acertou.')
        respostas_certas += 1
    else:
        print('Errou.')
    print()
qtd_perguntas = len(perguntas)
porcentagem_acertos = respostas_certas / qtd_perguntas * 100  # Porcetagem de acertos.

print(f'Você acertou {respostas_certas} pergunta(s).')
print(f'Você acertou {porcentagem_acertos}% das perguntas.')
