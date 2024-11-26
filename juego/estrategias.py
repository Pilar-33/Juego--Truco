import random

def jugador_aleatorio(mano: list, puntos_envido: int) -> dict:
    """
    Estrategia para el jugador aleatorio.
    Juega una carta aleatoria o canta envido/falta 
    envido según puntos.
    """

    if puntos_envido > 30:
        return "falta envido"
    if puntos_envido > 0:
        return "envido"
    carta_elegida = random.choice(mano)
    return carta_elegida

def jugador_estrategico(
    mano: list, puntos_envido: int, 
    carta_contraria: dict = None) -> dict | str:
    """
    Estrategia para el jugador estratégico.
    Canta envido si tiene más de 27 puntos o juega según jerarquía.
    """
    if puntos_envido > 27:
        return "envido"
    
    jugables = []
    if carta_contraria:
        for carta in mano:
            if carta["jerarquia"] >= carta_contraria["jerarquia"]:
                jugables.append(carta)
                
        if jugables:
            return min(jugables, key=lambda x: x["jerarquia"])
        else:
            return max(mano, key=lambda x: x["jerarquia"]) #cuando no puede ganar
    return max(mano, key=lambda x: x["jerarquia"]) #cuando juega primero