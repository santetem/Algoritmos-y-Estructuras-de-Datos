cantidad = int(input("Ingrese la cantidad de jugadores: "))
jugadores = []
puntaje = []
for _ in range (cantidad):
    nombres = input("Ingrese el nombre de cada jugador: ")
    jugadores.append(nombres)
    
for i in range(len(jugadores)):
    puntajeuno = int(input(f"Ingrese el puntaje del jugador {jugadores[i]}: "))
    puntaje.append(puntajeuno)

print("Los jugadores y su puntaje son: ")
print(jugadores)
print(puntaje)

