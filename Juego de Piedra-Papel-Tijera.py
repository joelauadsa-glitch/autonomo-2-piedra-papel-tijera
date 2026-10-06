# JUEGO PIEDRA, PAPEL O TIJERA

# Marcador
usuario1_puntos = 0
usuario2_puntos = 0

jugar = "si"

# Inicio del juego
while jugar == "si":

    print("   PIEDRA, PAPEL O TIJERA")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    # Ingresar la opción del Usuario 1
    usuario1 = int(input("\nIngrese la opción del Usuario 1 (1-3): "))

    # Validar la opción del Usuario 1
    if usuario1 < 1 or usuario1 > 3:
        print("Opción no válida. Intente nuevamente.")
        continue

    # Ingresar la opción del Usuario 2
    usuario2 = int(input("Ingrese la opción del Usuario 2 (1-3): "))

    # Validar la opción del Usuario 2
    if usuario2 < 1 or usuario2 > 3:
        print("Opción no válida. Intente nuevamente.")
        continue

    # Mostrar las elecciones
    if usuario1 == 1:
        nombre_usuario1 = "Piedra"
    elif usuario1 == 2:
        nombre_usuario1 = "Papel"
    else:
        nombre_usuario1 = "Tijera"

    if usuario2 == 1:
        nombre_usuario2 = "Piedra"
    elif usuario2 == 2:
        nombre_usuario2 = "Papel"
    else:
        nombre_usuario2 = "Tijera"

    print("\nUsuario 1 eligió:", nombre_usuario1)
    print("Usuario 2 eligió:", nombre_usuario2)

    # Comprobar si hay empate
    if usuario1 == usuario2:

        print("\nResultado: ¡Empate!")

    else:

        # Comprobar si gana el Usuario 1
        if (usuario1 == 1 and usuario2 == 3) or \
           (usuario1 == 2 and usuario2 == 1) or \
           (usuario1 == 3 and usuario2 == 2):

            usuario1_puntos += 1
            print("\n¡Usuario 1 gana!")
            print("Ganaste.")

        else:

            usuario2_puntos += 1
            print("\n¡Usuario 2 gana!")
            print("Perdiste.")

    # Mostrar el marcador
    print("MARCADOR")
    print("Usuario 1:", usuario1_puntos)
    print("Usuario 2:", usuario2_puntos)

    # Preguntar si desean jugar otra ronda
    jugar = input("\n¿Desean jugar otra ronda? (si/sí/s/no): ").lower()

    # El diagrama indica que Sí vuelve al inicio
    if jugar == "si" or jugar == "sí" or jugar == "s":
        jugar = "si"
    else:
        jugar = "no"

# Fin
print("          FIN DEL JUEGO")
print("Marcador final:")
print("Usuario 1:", usuario1_puntos)
print("Usuario 2:", usuario2_puntos)