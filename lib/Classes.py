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
