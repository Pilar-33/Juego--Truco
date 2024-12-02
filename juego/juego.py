from juego.cartas import*
from juego.estrategias import*
from juego.historial import*


def mostrar_menu() -> None:
    """Muestra el menú principal del juego"""
    print("""
        TRUCO ARGENTINO
    =====================
    1. Jugar partida
    2. Ver historial por jugador
    3. Ver historial por completo
    4. Salir """)

def obtener_datos_partida() -> tuple:
    """Obtiene los datos iniciales para comenzar una partida"""
    print("""
    Elige tu oponente:
    1. Jugador aleatorio
    2. Jugador estratégico """)
    tipo = "aleatorio" if input("Opción (1/2): ") == "1" else "estrategico"
    max_puntos = int(input("\nPuntos para ganar (15/30): "))
    return tipo, max_puntos

