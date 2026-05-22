import math


class OtimizadorRotas:
    def __init__(self, pontos):
        """
        pontos: lista de dicionários no formato:
        [
            {"id": 1, "x": 10, "y": 20},
            {"id": 2, "x": 15, "y": 5},
            ...
        ]
        """
        self.pontos = pontos

    def distancia_euclidiana(self, ponto_a, ponto_b):
        """
        Calcula a distância euclidiana entre dois pontos.
        """
        return math.sqrt(
            (ponto_b["x"] - ponto_a["x"]) ** 2 +
            (ponto_b["y"] - ponto_a["y"]) ** 2
        )

    def encontrar_rota(self, ponto_inicial_id=None):
        """
        Implementa o algoritmo do Vizinho Mais Próximo.

        Regras:
        - Começa em um ponto inicial
        - Vai para o ponto não visitado mais próximo
        - Repete até visitar todos
        - Retorna ao ponto inicial
        """

        if not self.pontos:
            return {
                "Ordem_rota": [],
                "Distância_total": 0
            }

        # Define ponto inicial
        if ponto_inicial_id is not None:
            atual = next(
                (p for p in self.pontos if p["id"] == ponto_inicial_id),
                None
            )

            if atual is None:
                raise ValueError("Ponto inicial não encontrado.")
        else:
            atual = self.pontos[0]

        ponto_inicial = atual

        nao_visitados = self.pontos.copy()
        nao_visitados.remove(atual)

        rota = [atual["id"]]
        distancia_total = 0

        while nao_visitados:
            proximo_ponto = min(
                nao_visitados,
                key=lambda ponto: self.distancia_euclidiana(atual, ponto)
            )

            distancia = self.distancia_euclidiana(atual, proximo_ponto)

            distancia_total += distancia
            rota.append(proximo_ponto["id"])

            atual = proximo_ponto
            nao_visitados.remove(proximo_ponto)

        # Retorna ao ponto inicial
        distancia_retorno = self.distancia_euclidiana(atual, ponto_inicial)
        distancia_total += distancia_retorno

        rota.append(ponto_inicial["id"])

        return {
            "Ordem_rota": rota,
            "Distância_total": round(distancia_total, 2)
        }


# =========================
# EXEMPLO DE USO
# =========================

pontos_entrega = [
    {"id": 1, "x": 10, "y": 10},
    {"id": 2, "x": 20, "y": 30},
    {"id": 3, "x": 15, "y": 25},
    {"id": 4, "x": 40, "y": 10},
    {"id": 5, "x": 25, "y": 5}
]

otimizador = OtimizadorRotas(pontos_entrega)

resultado = otimizador.encontrar_rota()

print(resultado)