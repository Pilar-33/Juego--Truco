import random

VALORES = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
PALOS = ["espada", "basto", "oro", "copa"]

def generar_mazo(VALORES, PALOS) -> list:
    """
    Genera el mazo completo con jerarquía de valores del Truco.
    Retorna una lista de diccionarios con información de cada carta.
    """

    jerarquia = {
    "1 espada": 14,  # Mejor carta
    "1 basto": 13,   # Segunda mejor
    "7 espada": 12,  # Tercera mejor
    "7 oro": 11,     # Cuarta mejor
    "3 espada": 10, 
    "3 oro": 10, 
    "3 copa": 10,
    "3 basto": 10,
    "2 espada": 9,
    "2 oro": 9,
    "2 copa": 9,
    "2 basto": 9,
    "1 oro": 8,
    "1 copa": 8,
    "12 espada": 7,
    "12 oro": 7,
    "12 copa": 7,
    "12 basto": 7,
    "11 espada": 6,
    "11 oro": 6,
    "11 copa": 6,
    "11 basto": 6,
    "10 espada": 5,
    "10 oro": 5,
    "10 copa": 5,
    "10 basto": 5,
    "7 copa": 4,
    "7 basto": 4,
    "6 espada": 3,
    "6 oro": 3,
    "6 copa": 3,
    "6 basto": 3,
    "5 espada": 2,
    "5 oro": 2,
    "5 copa": 2,
    "5 basto": 2,
    "4 espada": 1,
    "4 oro": 1,
    "4 copa": 1,
    "4 basto": 1
}

    mazo = []
    for palo in PALOS:
        for valor in VALORES:
            carta = {}
            carta["palo"] = palo
            carta["valor"] = valor
            clave = f"{valor} {palo}"
            carta["jerarquia"] = jerarquia[clave]
            mazo.append(carta)
    return mazo

def repartir_cartas(mazo: list) -> tuple:
    """
    Baraja el mazo y reparte 3 cartas a cada jugador.
    Retorna dos listas: una para cada jugador.
    """
    random.shuffle(mazo)
    cartas_jugador1 = mazo[:3]
    cartas_jugador2 = mazo[3:6]
    
    return cartas_jugador1, cartas_jugador2

def calcular_envido(mano: list) -> int:
    """
    Calcula el puntaje de envido para una mano.
    Retorna el puntaje máximo considerando cartas del mismo palo.
    """
    
    grupos_por_palo = {}
    for carta in mano:
        palo = carta["palo"]
        valor = carta["valor"]
        if valor > 7:
            valor = 0
            
        if palo not in grupos_por_palo:
            grupos_por_palo[palo] = []
        grupos_por_palo[palo].append(valor)
        
    #calcula puntaja maxima de los grupos de cartas
    puntos_maximos = 0
    for valores in grupos_por_palo.values():
        if len(valores) > 1:
            valores_ordenados = sorted(valores)
            dos_mayores = valores_ordenados[-2:]
            suma = sum(dos_mayores)
            puntos = suma + 20
            if puntos > puntos_maximos:
                puntos_maximos = puntos
                
    return puntos_maximos