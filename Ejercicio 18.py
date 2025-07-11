matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

def consigna(m):
    filas = len(m)
    columnas = len(m[0])

    transpuesta = []
    for j in range(columnas):
        nuevaFila = []
        for i in range(filas):
            nuevaFila.append(m[i][j])
        transpuesta.append(nuevaFila)
    
    return transpuesta

transpuesta = consigna(matriz)

print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)
