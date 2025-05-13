import tkinter as tk
from tkinter import messagebox
from backend.grafo import Grafo
from backend.json_manager import JsonManager
from backend.dijkstra import Dijkstra

class Vista:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Navegación WAZE")
        self.grafo = Grafo()
        self.grafo.cargar_grafo("mapa.json")

        self.setup_ui()

    def setup_ui(self):
        # Títulos y botones para interactuar con el grafo
        self.lbl_origen = tk.Label(self.root, text="Nodo de Origen:")
        self.lbl_origen.grid(row=0, column=0)

        self.entry_origen = tk.Entry(self.root)
        self.entry_origen.grid(row=0, column=1)

        self.lbl_destino = tk.Label(self.root, text="Nodo de Destino:")
        self.lbl_destino.grid(row=1, column=0)

        self.entry_destino = tk.Entry(self.root)
        self.entry_destino.grid(row=1, column=1)

        self.btn_calcular = tk.Button(self.root, text="Calcular Ruta", command=self.calcular_ruta)
        self.btn_calcular.grid(row=2, column=0, columnspan=2)

    def calcular_ruta(self):
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()

        if origen and destino:
            dijkstra = Dijkstra(self.grafo.obtener_grafo())
            ruta = dijkstra.calcular_ruta(origen, destino)

            messagebox.showinfo("Ruta Encontrada", f"La ruta más corta es: {' -> '.join(ruta)}")
        else:
            messagebox.showerror("Error", "Por favor ingrese ambos nodos (origen y destino).")

if __name__ == "__main__":
    root = tk.Tk()
    app = Vista(root)
    root.mainloop()
