import csv

def guardar_historial(resultado: dict, archivo: str = "historial.csv") -> None:
    """Guarda el resultado de la partida en un archivo CSV."""
    with open(archivo, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([resultado["jugador"], resultado["oponente"], resultado["puntos_jugador"], resultado["puntos_oponente"]])

def leer_historial(nombre_archivo: str) -> list[tuple[str, str, int, int]]:
    """
    Lee el historial de partidas desde un archivo CSV.

    Args:
        nombre_archivo (str): Nombre del archivo que contiene el historial.

    Returns:
        list[tuple[str, str, int, int]]: Lista de partidas como tuplas 
        con datos de jugadores y puntos.
    """
    partidas = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            jugador, oponente, puntos_jugador, puntos_oponente = linea.strip().split(',')
            partidas.append((jugador, oponente, int(puntos_jugador), int(puntos_oponente)))
    return partidas


def mostrar_historial(nombre_archivo: str) -> None:
    """
    Muestra el historial completo de todas las partidas.

    Args:
        nombre_archivo (str): Nombre del archivo que contiene el historial.
    """
    partidas = leer_historial(nombre_archivo)
    for jugador, oponente, puntos_jugador, puntos_oponente in partidas:
        print(f"\nResultado de la partida:")
        print(f"{jugador}: {puntos_jugador} puntos")
        print(f"{oponente}: {puntos_oponente} puntos")
        if puntos_jugador > puntos_oponente:
            print(f"¡{jugador} ganó la partida!")
        else:
            print(f"¡{oponente} ganó la partida!")
        print("-" * 30)

            
def filtrar_partidas_jugador(nombre_archivo: str, nombre_jugador: str) -> list[dict]:
    """
    Filtra las partidas de un jugador específico desde un archivo CSV.

    Args:
        nombre_archivo (str): Nombre del archivo que contiene el historial.
        nombre_jugador (str): Nombre del jugador a buscar.

    Returns:
        list[dict]: Lista de partidas filtradas, cada una con el oponente y puntajes.
    """
    partidas = []
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo:
            jugador, oponente, puntos_jugador, puntos_oponente = linea.strip().split(',')
            if jugador == nombre_jugador:
                partidas.append({
                    "oponente": oponente,
                    "puntos_jugador": int(puntos_jugador),
                    "puntos_oponente": int(puntos_oponente)
                })
    return partidas


def mostrar_historial_jugador(nombre_jugador: str) -> None:
    """
    Muestra el historial de partidas de un jugador específico.

    Args:
        nombre_jugador (str): Nombre del jugador a buscar.
    """
    partidas = filtrar_partidas_jugador("historial.csv", nombre_jugador)
    if partidas:
        print(f"\nHistorial de partidas de {nombre_jugador}:")
        for i, partida in enumerate(partidas, 1):
            print(f"\nPartida {i}:")
            print(f"{nombre_jugador}: {partida['puntos_jugador']} puntos")
            print(f"{partida['oponente']}: {partida['puntos_oponente']} puntos")
            if partida['puntos_jugador'] > partida['puntos_oponente']:
                print(f"¡{nombre_jugador} ganó!")
            else:
                print(f"¡{partida['oponente']} ganó!")
        
        print("\nÚltima partida jugada:")
        ultima = partidas[-1]
        print(f"{nombre_jugador}: {ultima['puntos_jugador']} puntos")
        print(f"{ultima['oponente']}: {ultima['puntos_oponente']} puntos")
        if ultima['puntos_jugador'] > ultima['puntos_oponente']:
            print(f"¡{nombre_jugador} ganó la partida!")
        else:
            print(f"¡{ultima['oponente']} ganó la partida!")
    else:
        print(f"\nNo se encontraron partidas para {nombre_jugador}.")

