import csv

def guardar_historial(resultado: dict, archivo: str = "historial.csv") -> None:
    """Guarda el resultado de la partida en un archivo CSV."""
    with open(archivo, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([resultado["jugador"], resultado["oponente"], resultado["puntos_jugador"], resultado["puntos_oponente"]])

def leer_historial(nombre_archivo: str) -> list:
    """
    Lee el historial de partidas desde un archivo CSV.

    Args:
        nombre_archivo (str): Nombre del archivo que contiene el historial.

    Returns:
        list: Lista de partidas como tuplas 
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
    for num_partida, (jugador, oponente, puntos_jugador, puntos_oponente) in enumerate(partidas, 1):
        print(f"""
                RESULTADO DE LA PARTIDA N°{num_partida}
            ------------------------------------
            \t{jugador}: {puntos_jugador} puntos
            \t{oponente}: {puntos_oponente} puntos""")

        if puntos_jugador > puntos_oponente:
            print(f"\t\t¡{jugador} ganó la partida!")
        else:
            print(f"\t\t¡{oponente} ganó la partida!")
            
    
            
def filtrar_partidas_jugador(
    nombre_archivo: str, 
    nombre_jugador: str) -> list:
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
        print(f"""
        HISTORIAL DE PARTIDAS DE {nombre_jugador}
        ==================================""")
        for i, partida in enumerate(partidas, 1):
            print(f"""
                    PARTIDA {i}
            =======================
            {nombre_jugador}: {partida['puntos_jugador']} puntos.
            {partida['oponente']}: {partida['puntos_oponente']} puntos.""")
            if partida['puntos_jugador'] > partida['puntos_oponente']:
                print(f"\t\t¡{nombre_jugador} ganó!")
            else:
                print(f"\t\t¡{partida['oponente']} ganó!")
        
        print("\n\tÚLTIMA PARTIDA JUGADA:")
        print("\t=======================")
        ultima = partidas[-1]
        print(f"\t{nombre_jugador}: {ultima['puntos_jugador']} puntos")
        print(f"\t{ultima['oponente']}: {ultima['puntos_oponente']} puntos")
        if ultima['puntos_jugador'] > ultima['puntos_oponente']:
            print(f"\t¡{nombre_jugador} ganó la partida!")
        else:
            print(f"\t¡{ultima['oponente']} ganó la partida!")
    else:
        print(f"\n\tNo se encontraron partidas para {nombre_jugador}.")

