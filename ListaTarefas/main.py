
from opcaoTarefas import addTarefas, listarTarefas, desfazer, refazer

tarefas = []
excluidos = []

while True:

    print("#" * 50)
    print("1. Adicione uma tarefa.")
    print("2. Liste suas tarefas.")
    print("3. Desfaça sua última alteração.")
    print("4. Refaça sua última alteração")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        novaTarefa = input("Digite sua nova tarefa: ")
        addTarefas(tarefas, novaTarefa)
        continue
    elif opcao == '2':
        print("Tarefas:")
        listarTarefas(tarefas)
        print()
        continue
    elif opcao == '3':
        desfazer(tarefas, excluidos)
        continue
    elif opcao == '4':
        refazer(tarefas, excluidos)
        continue
    else:
        print("Opção inválida. Tente novamente.")
        continue
