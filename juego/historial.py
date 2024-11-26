import csv

def guardar_historial(resultado: dict, archivo: str = "historial.csv") -> None:
    """Guarda el resultado de la partida en un archivo CSV."""
    with open(archivo, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([resultado["jugador"], resultado["oponente"], resultado["puntos_jugador"], resultado["puntos_oponente"]])

def mostrar_historial() -> None:
    """
    Muestra el historial completo de todas las partidas
    """
    with open("historial.csv", "r") as archivo:
        for linea in archivo:
            jugador, oponente, puntos_jugador, puntos_oponente = linea.strip().split(',')
            print(f"\nResultado de la partida:")
            print(f"{jugador}: {puntos_jugador} puntos")
            print(f"{oponente}: {puntos_oponente} puntos")
            if int(puntos_jugador) > int(puntos_oponente):
                print(f"¡{jugador} ganó la partida!")
            else:
                print(f"¡{oponente} ganó la partida!")
            print("-" * 30)
            
def mostrar_historial_jugador(nombre_jugador):
    """
    Muestra el historial de partidas de un jugador específico
    
    Args:
        nombre_jugador (str): Nombre del jugador a buscar
        
    Muestra:
        - Todas las partidas del jugador
        - Puntajes obtenidos
        - Resultado de cada partida
        - Última partida jugada
    """
    partidas = []
    with open("historial.csv", "r") as archivo:
        for linea in archivo:
            jugador, oponente, puntos_jugador, puntos_oponente = linea.strip().split(',')
            if jugador == nombre_jugador:
                partidas.append({
                    "oponente": oponente,
                    "puntos_jugador": int(puntos_jugador),
                    "puntos_oponente": int(puntos_oponente)
                })
    
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
        print(f"\nNo se encontraron partidas para {nombre_jugador}")

