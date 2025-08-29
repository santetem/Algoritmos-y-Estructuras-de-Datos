import random

inventario = {
    'Perifericos': {'Teclado': 1, 'Mouse': 1, 'Monitor': 1, 'Auricular': 3},
    'Hardware': {'PlacaMadre': 2, 'Procesador': 2, 'SSD': 2, 'RAM': 4, 'Fuente': 2, 'Grafica': 3},
    'Celulares': {'Samsung': 8, 'iPhone': 7, 'Motorola': 5, 'Xiaomi': 11}
}

print("----------------------------------------")
print("Su inventario de productos es:")
for i in inventario:
    print(i, inventario[i])
print("----------------------------------------")


categoria = list(inventario.keys())
catRandom = random.choice(categoria)

for _ in range(3):
    lista = list(inventario[catRandom].keys())
    proRandom = random.choice(lista)
    actualizado = inventario[catRandom][proRandom] - 1
    inventario[catRandom][proRandom] = actualizado
    if actualizado > 0:
        print(f"Se acaba de vender un {proRandom}, quedan {actualizado}.")
    else:
        inventario[catRandom].pop(proRandom)
        print(f"Se terminó el stock de {proRandom}.")
        
print("----------------------------------------")
print(f"Su nuevo inventario es:")
for i in inventario:
    print(i, inventario[i])


while True: 
    print("Ingrese la opción deseada")
    print("1 - Agregar un nuevo producto al inventario")
    print("2 - Agregar stock a un producto existente")
    print("3 - Ver el inventario")
    deseo = input("> ")

    
    if deseo == '1':
        nuevopro = input("Ingrese el nombre del producto que desea agregar a su inventario: ")

        print("¿A qué categoría desea agregarlo?")
        categorias = list(inventario.keys())
        print("1 - Perifericos")
        print("2 - Hardware")
        print("3 - Celulares")
        
        categoriaElegida = input("> ")

        if categoriaElegida == '1' or '2' or '3':
            categoriaElegida = categorias[int(categoriaElegida) - 1]
            print(f"Ha elegido la categoría {categoriaElegida}")
            cantidadpro = int(input("Ingrese el stock de su producto nuevo: "))
            inventario[categoriaElegida][nuevopro] = cantidadpro
            print("El inventario se ha actualizado correctamente.")
        else:
            print("No existe una categoría con ese número.")

    elif deseo == '2':
        catElegida = input("Elija la categoría que desea reponer: ")
        if catElegida in inventario:
            print(f"Esta categoría tiene:")
            print(inventario[catElegida])
            pordi = input("Elija el producto que desea reponer: ")
            if pordi in inventario[catElegida]:
                numeroReposicion = int(input("Ingrese cuánto stock quiere reponer: "))
                inventario[catElegida][pordi] += numeroReposicion
                print("El inventario se ha actualizado correctamente.")
            else:
                print("El producto no está en el inventario.")
        else: 
            print("La categoría no está en el inventario.")


    elif deseo == '3':
        print("Su inventario es: ")
        for i in inventario:
            print(i, inventario[i])

    else:
        print("Opción no válida. Intenta otra vez.")