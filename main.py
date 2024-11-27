from os import system
system("cls")
from juego.juego import*
from juego.historial import*

juego = True
while juego == True:
    opcion = input("""
    BIENVENIDO AL TRUCO
    =======================
    1. Jugar nueva partida.
    2. Mi historial.
    3. Hstorial general.
    4. Salir.
    Seleccione una opción: """)


    match opcion:
        case "1":
            nombre_jugador = input("Ingrese su nombre: ")
            tipo_oponente = input("Elija el tipo de oponente (aleatorio/estrategico): ").lower()
            puntos_maximos = int(input("Ingrese los puntos máximos de la partida (15 o 30): "))

            resultado = jugar_partida(nombre_jugador, tipo_oponente, puntos_maximos)
            print(f"""
            RESULTADOS DE LA PARTIDA:
            ===========================
            Jugador: {resultado['jugador']}
            Oponente: {resultado['oponente']}
            Puntos jugador: {resultado['puntos_jugador']}
            Puntos oponente: {resultado['puntos_oponente']}
            """)
            if resultado['puntos_jugador'] > resultado['puntos_oponente']:
                print(f"\n¡{resultado['jugador']} ganó la partida!")
            else:
                print(f"\n¡{resultado['oponente']} ganó la partida!")
        case "2":
            nombre = input("Ingrese su nombre: ")
            filtrar_partidas_jugador("historial.csv", nombre)
            mostrar_historial_jugador(nombre)
        case "3":
            print("\nHistorial general de partidas:")
            leer_historial("historial.csv")
            mostrar_historial("historial.csv")
        case "4":
            print("¡Gracias por jugar!")
            juego = False

