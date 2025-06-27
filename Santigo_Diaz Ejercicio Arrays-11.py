arreglo = [1, 3, 1, 5, 6, 4, 8, 7, 9, 10]
rupturas = 0

for i in range(len(arreglo) - 1):
    if arreglo[i] > arreglo[i + 1]:
        rupturas += 1

print(rupturas)