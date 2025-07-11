matriz = [
    [1, 2, 8],
    [3, 4, 5],
    [9, 7, 6]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

def consigna(matriz):
    filas = len(matriz)
    if filas == 0:
        return

    columnas = len(matriz[0])
    if columnas == 0:
        return

    variable = matriz[0][0]

    for i in range(filas):
        for j in range(columnas):
            if j < columnas - 1: 
                matriz[i][j] = matriz[i][j+1]
            else: 
                if i < filas - 1:
                    matriz[i][j] = matriz[i+1][0]
                else:
                    matriz[i][j] = variable


consigna(matriz)

print("Matriz modificada después de la rotación:")
for fila in matriz:
    print(fila)