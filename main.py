from lib import *
print('\033[91m Matriz de adyacencia\033[0m')
print(df)
print('\033[91m Lista de relaciones:\033[0m')

print(cadena[:-2]) 


mi_grafo = grafo()
[mi_grafo.addArista(origen, destino, peso) for origen, destino, peso in aristas]

    
print("\033[91m Grafo:\033[0m")
print("Vértices:", vertices)
print(mi_grafo)

inicio = 'B'
fin = 'H'
path, peso_total = mi_grafo.caminoMasCorto(inicio, fin)

mi_grafo.mostrarPath(inicio)

print(f"\nEl camino más corto desde {inicio} hasta {fin}:")
print(" -> ".join(path))
print(f"Peso Total: {peso_total}")