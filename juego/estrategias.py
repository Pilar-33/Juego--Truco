import random

def jugador_aleatorio(puntos_envido: int) -> str:
    """
    Estrategia para el jugador aleatorio.
    Puede cantar envido, real envido o falta envido aleatoriamente.
    """
    opciones = ["no", "envido"]
    if puntos_envido > 27:
        opciones.append("real envido")
    if puntos_envido > 30:
        opciones.append("falta envido")
    return random.choice(opciones)

def jugador_estrategico(
    mano: list, puntos_envido: int, 
    carta_contraria: dict = None) -> dict:
    """
    Estrategia para el jugador estratégico.
    Canta variantes del envido si tiene puntos altos 
    y juega cartas según jerarquía.
    """
    if puntos_envido > 30:
        return "falta envido"
    elif puntos_envido > 27:
        return "real envido"
    elif puntos_envido > 20:
        return "envido"
    elif puntos_envido > 15:
        return "no"

    jugables = []
    if carta_contraria:
        for carta in mano:
            if carta["jerarquia"] >= carta_contraria["jerarquia"]:
                jugables.append(carta)
        return min(jugables, key=lambda x: x["jerarquia"]) if jugables else max(mano, key=lambda x: x["jerarquia"])
    return max(mano, key=lambda x: x["jerarquia"])
