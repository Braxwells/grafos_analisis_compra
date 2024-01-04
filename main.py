import networkx as nx
import matplotlib.pyplot as plt

class AnalisisCompras:
    def __init__(self):
        self.productos = []
        self.matriz_conexiones = []
        self.transacciones = [
            ["Pan", "Leche"],
            ["Pan", "Mermelada"],
            ["Leche", "Galletas"],
            ["Pan", "Leche", "Galletas"],
            ["Mermelada", "Galletas"]
        ]

    def identificar_productos(self):
        for transaccion in self.transacciones:
            for producto in transaccion:
                if producto not in self.productos:
                    self.productos.append(producto)
        print("Productos:", self.productos)
        self.establecer_conexiones()

    def establecer_conexiones(self):
        for i in range(len(self.productos)):
            self.matriz_conexiones.append([0] * len(self.productos))

        for transaccion in self.transacciones:
            for i in range(len(transaccion) - 1):
                index1 = self.productos.index(transaccion[i])
                index2 = self.productos.index(transaccion[i + 1])
                self.matriz_conexiones[index1][index2] += 1

        print("Matriz de conexiones:")
        for row in self.matriz_conexiones:
            print(row)

    def encontrar_pares_populares(self):
        max_frecuencia = 0
        pares_populares = []

        for i in range(len(self.productos)):
            for j in range(i + 1, len(self.productos)):
                frecuencia = self.matriz_conexiones[i][j]
                if frecuencia > max_frecuencia:
                    max_frecuencia = frecuencia
                    pares_populares = [(self.productos[i], self.productos[j])]
                elif frecuencia == max_frecuencia:
                    pares_populares.append((self.productos[i], self.productos[j]))

        print("Pares más populares de productos comprados juntos:", pares_populares)

    def graficar_red_compras(self):
        G = nx.Graph()

        for producto in self.productos:
            G.add_node(producto)

        for i in range(len(self.productos)):
            for j in range(i + 1, len(self.productos)):
                if self.matriz_conexiones[i][j] > 0:
                    G.add_edge(self.productos[i], self.productos[j], weight=self.matriz_conexiones[i][j])

        pos = nx.spring_layout(G)  # Posicionamiento de los nodos
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

# Uso de la clase personalizada
analisis_compras = AnalisisCompras()
analisis_compras.identificar_productos()
analisis_compras.encontrar_pares_populares()
analisis_compras.graficar_red_compras()
