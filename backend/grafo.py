import json

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = {}

    def eliminar_nodo(self, nodo):
        if nodo in self.grafo:
            del self.grafo[nodo]
            for nodo_destino in self.grafo:
                if nodo in self.grafo[nodo_destino]:
                    del self.grafo[nodo_destino]

    def agregar_arista(self, nodo_origen, nodo_destino, peso):
        if nodo_origen in self.grafo and nodo_destino in self.grafo:
            self.grafo[nodo_origen][nodo_destino] = peso
            self.grafo[nodo_destino][nodo_origen] = peso  # Para grafos no dirigidos

    def eliminar_arista(self, nodo_origen, nodo_destino):
        if nodo_origen in self.grafo and nodo_destino in self.grafo[nodo_origen]:
            del self.grafo[nodo_origen][nodo_destino]
            del self.grafo[nodo_destino][nodo_origen]

    def obtener_grafo(self):
        return self.grafo

    def guardar_grafo(self, archivo):
        with open(archivo, 'w') as f:
            json.dump(self.grafo, f, indent=4)

    def cargar_grafo(self, archivo):
        with open(archivo, 'r') as f:
            self.grafo = json.load(f)
