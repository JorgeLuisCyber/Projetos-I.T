from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
import json
import os

app = FastAPI(title="API de Gerenciador de Tarefas")

ARQUIVO = "tarefas.json"


# =========================
# MODELOS
# =========================

class Tarefa(BaseModel):
    titulo: str
    concluida: bool = False


class AtualizarTarefa(BaseModel):
    titulo: str | None = None
    concluida: bool | None = None


# =========================
# FUNÇÕES AUXILIARES
# =========================

def carregar_tarefas():
    if not os.path.exists(ARQUIVO):
        return []

    with open(ARQUIVO, "r", encoding="utf-8") as f:
        return json.load(f)


def salvar_tarefas(tarefas):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


# =========================
# ROTAS
# =========================

# GET -> Listar tarefas
@app.get("/tarefas", status_code=status.HTTP_200_OK)
def listar_tarefas():
    return carregar_tarefas()


# GET -> Buscar tarefa por ID
@app.get("/tarefas/{tarefa_id}", status_code=status.HTTP_200_OK)
def obter_tarefa(tarefa_id: int):
    tarefas = carregar_tarefas()

    if tarefa_id < 0 or tarefa_id >= len(tarefas):
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    return tarefas[tarefa_id]


# POST -> Criar tarefa
@app.post("/tarefas", status_code=status.HTTP_201_CREATED)
def criar_tarefa(tarefa: Tarefa):
    tarefas = carregar_tarefas()

    nova_tarefa = tarefa.dict()

    tarefas.append(nova_tarefa)
    salvar_tarefas(tarefas)

    return {
        "mensagem": "Tarefa criada com sucesso",
        "tarefa": nova_tarefa
    }


# PATCH -> Atualizar parcialmente
@app.patch("/tarefas/{tarefa_id}", status_code=status.HTTP_200_OK)
def atualizar_tarefa(tarefa_id: int, dados: AtualizarTarefa):
    tarefas = carregar_tarefas()

    if tarefa_id < 0 or tarefa_id >= len(tarefas):
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    tarefa = tarefas[tarefa_id]

    if dados.titulo is not None:
        tarefa["titulo"] = dados.titulo

    if dados.concluida is not None:
        tarefa["concluida"] = dados.concluida

    tarefas[tarefa_id] = tarefa
    salvar_tarefas(tarefas)

    return {
        "mensagem": "Tarefa atualizada",
        "tarefa": tarefa
    }


# DELETE -> Remover tarefa
@app.delete("/tarefas/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_tarefa(tarefa_id: int):
    tarefas = carregar_tarefas()

    if tarefa_id < 0 or tarefa_id >= len(tarefas):
        raise HTTPException(
            status_code=404,
            detail="Tarefa não encontrada"
        )

    tarefas.pop(tarefa_id)
    salvar_tarefas(tarefas)

    return