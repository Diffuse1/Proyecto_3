from .fuc import *
class grafo:
    def __init__(self):
        self.Aristas = {}

    def addVertice(self, vertice):
        self.Aristas[vertice] = {}

    def addArista(self, origen, destino, peso):
        if origen not in self.Aristas:
            self.addVertice(origen)
        if destino not in self.Aristas:
            self.addVertice(destino)
        self.Aristas[origen].update({destino: peso})

    def __str__(self):
        return printDicc(self.Aristas)
    
    def dijkstra(self, origen):
        etiquetas = {v: float('inf') for v in self.Aristas}
        padres = {v: None for v in self.Aristas}
        etiquetas[origen] = 0
        vertices_no_visitados = list(self.Aristas.keys())

        while vertices_no_visitados:
            # Encontrar el vértice con la etiqueta mínima
            min_etiqueta = float('inf')
            min_vertice = None
            for v in vertices_no_visitados:
                if etiquetas[v] < min_etiqueta:
                    min_etiqueta = etiquetas[v]
                    min_vertice = v

            if min_vertice is None:
                break

            vertices_no_visitados.remove(min_vertice)

            # Actualizar las etiquetas de los vecinos
            for vecino, peso_vecino in self.Aristas[min_vertice].items():
                etiqueta_nueva = etiquetas[min_vertice] + peso_vecino
                if etiqueta_nueva < etiquetas[vecino]:
                    etiquetas[vecino] = etiqueta_nueva
                    padres[vecino] = min_vertice

        return etiquetas, padres

    def caminoMasCorto(self, origen, destino):
        etiquetas, padres = self.dijkstra(origen)
        camino = []
        peso_total = etiquetas[destino]

        while destino:
            camino.append(destino)
            destino = padres[destino]

        camino.reverse()
        return camino, peso_total

    def mostrarPath(self, origen):
        etiquetas, _ = self.dijkstra(origen)
        print("Etiquetas en cada vértice (Path):")
        for v, etiqueta in etiquetas.items():
            print(f"{v}: {etiqueta}")
