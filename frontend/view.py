import tkinter as tk
from tkinter import messagebox
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
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

        self.btn_mostrar_grafo = tk.Button(self.root, text="Mostrar Grafo", command=self.mostrar_grafo)
        self.btn_mostrar_grafo.grid(row=3, column=0, columnspan=2)

        # Lienzo para la visualización del grafo
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.grid(row=4, column=0, columnspan=2)

    def calcular_ruta(self):
        origen = self.entry_origen.get()
        destino = self.entry_destino.get()

        if origen and destino:
            dijkstra = Dijkstra(self.grafo.obtener_grafo())
            ruta = dijkstra.calcular_ruta(origen, destino)

            messagebox.showinfo("Ruta Encontrada", f"La ruta más corta es: {' -> '.join(ruta)}")
        else:
            messagebox.showerror("Error", "Por favor ingrese ambos nodos (origen y destino).")

    def mostrar_grafo(self):
        # Crear un grafo de NetworkX
        G = nx.Graph()

        # Agregar nodos y aristas del grafo
        for nodo, conexiones in self.grafo.obtener_grafo().items():
            G.add_node(nodo)
            for vecino, peso in conexiones.items():
                G.add_edge(nodo, vecino, weight=peso)

        # Crear la figura para el grafo
        plt.figure(figsize=(8, 6))
        pos = nx.spring_layout(G)  # Diseño del grafo

        # Dibujar el grafo
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10, font_weight='bold')
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        # Integrar el grafo con Tkinter usando Matplotlib
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()  # Limpiar el lienzo antes de mostrar el grafo

        canvas = FigureCanvasTkAgg(plt.gcf(), master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = Vista(root)
    root.mainloop()
