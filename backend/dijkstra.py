import heapq

class Dijkstra:
    def __init__(self, grafo):
        self.grafo = grafo

    def calcular_ruta(self, origen, destino, paradas=[]):
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[origen] = 0
        previos = {nodo: None for nodo in self.grafo}
        cola_prioridad = [(0, origen)]
        ruta = []

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if nodo_actual == destino:
                break

            for vecino, peso in self.grafo[nodo_actual].items():
                nueva_distancia = distancia_actual + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    previos[vecino] = nodo_actual
                    heapq.heappush(cola_prioridad, (nueva_distancia, vecino))

        # Construir la ruta
        nodo = destino
        while nodo is not None:
            ruta.insert(0, nodo)
            nodo = previos[nodo]

        # Si hay paradas intermedias, verificar que sean parte de la ruta
        if paradas:
            ruta_final = []
            for parada in paradas:
                if parada in ruta:
                    ruta_final.append(parada)
            return ruta_final
        else:
            return ruta
