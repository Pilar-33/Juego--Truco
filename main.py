from os import system
system("cls")
from juego.juego import*
from juego.historial import*
from juego.jugar_partida import*


juego = True
while juego == True:
    mostrar_menu()
    opcion = input("""Seleccione una opcion: """)

    match opcion:
        case "1":
            nombre = input("Ingrese su nombre: ")
            tipo, max_puntos = obtener_datos_partida()
            jugar_partida(nombre, tipo, max_puntos)
        case "2":
            nombre = input("Ingrese su nombre: ")
            filtrar_partidas_jugador("historial.csv", nombre)
            mostrar_historial_jugador(nombre)
        case "3":
            print(f"""
            HISTORIAL GENERAL DE PARTIDAS
            ===========================""")
            leer_historial("historial.csv")
            mostrar_historial("historial.csv")
        case "4":
            print("¡Gracias por jugar!")
            juego = False

