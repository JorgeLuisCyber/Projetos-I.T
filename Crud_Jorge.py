import json
import os

ARQUIVO = "tarefas.json"


def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []
    with open(ARQUIVO, "r") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w") as f:
        json.dump(tarefas, f, indent=4)


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, tarefa in enumerate(tarefas, 1):
        status = "✔" if tarefa["concluida"] else "✗"
        print(f"{i}. [{status}] {tarefa['titulo']}")


def adicionar_tarefa(tarefas):
    titulo = input("Digite o título da tarefa: ")
    tarefas.append({"titulo": titulo, "concluida": False})
    salvar_tarefas(tarefas)
    print("Tarefa adicionada!")


def atualizar_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        i = int(input("Número da tarefa para atualizar: ")) - 1
        if 0 <= i < len(tarefas):
            novo_titulo = input("Novo título: ")
            tarefas[i]["titulo"] = novo_titulo
            salvar_tarefas(tarefas)
            print("Tarefa atualizada!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")


def concluir_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        i = int(input("Número da tarefa concluída: ")) - 1
        if 0 <= i < len(tarefas):
            tarefas[i]["concluida"] = True
            salvar_tarefas(tarefas)
            print("Tarefa marcada como concluída!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")


def deletar_tarefa(tarefas):
    listar_tarefas(tarefas)
    try:
        i = int(input("Número da tarefa para deletar: ")) - 1
        if 0 <= i < len(tarefas):
            tarefas.pop(i)
            salvar_tarefas(tarefas)
            print("Tarefa removida!")
        else:
            print("Índice inválido.")
    except ValueError:
        print("Entrada inválida.")


def menu():
    tarefas = carregar_tarefas()

    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Listar tarefas")
        print("2. Adicionar tarefa")
        print("3. Atualizar tarefa")
        print("4. Concluir tarefa")
        print("5. Deletar tarefa")
        print("0. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            listar_tarefas(tarefas)
        elif opcao == "2":
            adicionar_tarefa(tarefas)
        elif opcao == "3":
            atualizar_tarefa(tarefas)
        elif opcao == "4":
            concluir_tarefa(tarefas)
        elif opcao == "5":
            deletar_tarefa(tarefas)
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()