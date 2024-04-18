import pandas as pd

def printDicc(dicc):
    for i in dicc:
        print(f'Vertice: {i}')
        for j in dicc[i]:
            print(f'\tDestino: {j} \t\tPeso: {dicc[i][j]}')
    return ''


nombre_archivo = input('Ingrese el nombre del archivo "Eval.xlsx": ')

df = pd.read_excel(nombre_archivo,index_col=0)

vertices = df.columns.tolist()
aristas = []

for i in range(df.shape[0]):
    origen = df.index[i]
    for j in range(df.shape[1]):
        destino = df.columns[j]
        peso = df.iloc[i, j]
        if pd.notna(peso) and peso != 0:
            aristas.append((origen, destino, peso))

            
cadena = ""
for arista in aristas:
    cadena += f"[{arista[0]}] -> [{arista[1]}] : Peso [{arista[2]}], "
