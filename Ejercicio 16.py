matriz1 = [
    [10, 8],
    [6, 4]
]

matriz2 = [
    [1, 2],
    [3, 4]
]

print("Matriz 1 original:")
for fila in matriz1:
    print(fila)

print("\nMatriz 2 original:")
for fila in matriz2:
    print(fila)

def restar_matrices_consigna(m1, m2):
    filas_m1 = len(m1)
    columnas_m1 = len(m1[0])

    resultado = []
    for i in range(filas_m1):
        fila_resultado = []
        for j in range(columnas_m1):
            fila_resultado.append(m1[i][j] - m2[i][j])
        resultado.append(fila_resultado)

    return resultado

matriz_resta = restar_matrices_consigna(matriz1, matriz2)

print("La resta de las matrices es:")
for fila in matriz_resta:
    print(fila)