def addTarefas(listaTarefas, novaTarefa):
    listaTarefas.append(novaTarefa)


def listarTarefas(listaTarefas):
    for i in listaTarefas:
        print(i)


def desfazer(listaTarefas, listaExcluidos):
    try:
        excluido = listaTarefas.pop()
        listaExcluidos.append(excluido)
    except:
        print("Não há nada para excluir.")


def refazer(listaTarefas, listaExcluidos):
    try:
        ultimoExcluido = listaExcluidos.pop()
        listaTarefas.append(ultimoExcluido)
    except:
        print("Nada a ser refeito")