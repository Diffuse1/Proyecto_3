from lib import *
print('\033[91m Matriz de adyacencia\033[0m')
print(df)
print('\033[91m Lista de relaciones:\033[0m')
for arista in aristas:
    print(f"{arista[0]} -> {arista[1]} : Peso {arista[2]}")


mi_grafo = grafo()
for origen, destino, peso in aristas:
    mi_grafo.addArista(origen, destino, peso)
    
print("\033[91m Grafo:\033[0m")
print("Vértices:", vertices)
print(mi_grafo)
