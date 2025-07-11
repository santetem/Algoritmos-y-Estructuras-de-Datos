matriz1 = [
    [1, 2],
    [3, 4]
]

matriz2 = [
    [5, 6],
    [7, 8]
]

print("Matriz 1 original:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2 original:")
for fila in matriz2:
    print(fila)

def consigna(m1, m2):
    filas_m1 = len(m1)
    columnas_m1 = len(m1[0])
    filas_m2 = len(m2)
    columnas_m2 = len(m2[0])

    if columnas_m1 != filas_m2:
        print("El número de columnas de la primera matriz debe ser igual al número de filas de la segunda.")
        return None

    resultado = []
    for _ in range(filas_m1):
        resultado.append([0] * columnas_m2)

    for i in range(filas_m1):
        for j in range(columnas_m2):
            for k in range(columnas_m1):
                resultado[i][j] += m1[i][k] * m2[k][j]

    return resultado

matrizProducto = consigna(matriz1, matriz2)

if matrizProducto is not None:
    print("El producto de las matrices es:")
    for fila in matrizProducto:
        print(fila)
