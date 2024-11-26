from juego.cartas import*
from juego.estrategias import*
from juego.historial import*


def manejar_envido(tipo_oponente: str, envido_jugador: int, envido_oponente: int) -> tuple[int, int]:
    """
    Maneja la lógica del envido según el tipo de oponente.
    
    Args:
        tipo_oponente: Tipo de oponente ('aleatorio' o 'estrategico')
        envido_jugador: Puntos de envido del jugador
        envido_oponente: Puntos de envido del oponente
        
    Returns:
        tuple: (puntos_jugador, puntos_oponente) Puntos ganados por envido
    """
    puntos_jugador = 0
    puntos_oponente = 0
    
    print(f"\nTus puntos de envido: {envido_jugador}")

    if tipo_oponente == "aleatorio":
        if envido_oponente > 30:
            print("\nOponente canta: ¡Falta envido!")
            respuesta = input("¿Aceptas? (si/no): ").lower()
            if respuesta == "si":
                if envido_jugador > envido_oponente:
                    puntos_jugador += 3
                    print("¡Ganaste el envido!")
                else:
                    puntos_oponente += 3
                    print("¡Perdiste el envido!")
        elif envido_oponente > 27:
            print("\nOponente canta: ¡Envido!")
            respuesta = input("¿Aceptas? (si/no): ").lower()
            if respuesta == "si":
                if envido_jugador > envido_oponente:
                    puntos_jugador += 2
                    print("¡Ganaste el envido!")
                else:
                    puntos_oponente += 2
                    print("¡Perdiste el envido!")

    elif tipo_oponente == "estrategico":
        if envido_oponente > 27:
            print("\nOponente canta: ¡Envido!")
            respuesta = input("¿Aceptas? (si/no): ").lower()
            if respuesta == "si":
                if envido_jugador > envido_oponente:
                    puntos_jugador += 2
                    print("¡Ganaste el envido!")
                else:
                    puntos_oponente += 2
                    print("¡Perdiste el envido!")
                    
    return puntos_jugador, puntos_oponente

def obtener_carta_valida(num_cartas: int) -> int:
    """
    Obtiene y valida la selección de carta del usuario.
    
    Args:
        num_cartas: Número de cartas disponibles
        
    Returns:
        int: Índice válido de la carta seleccionada
    """
    while True:
        try:
            seleccion = input(f"Seleccione la carta a jugar (1-{num_cartas}): ")
            if seleccion.strip() == "":
                continue
            carta_index = int(seleccion) - 1
            if 0 <= carta_index < num_cartas:
                return carta_index
            print(f"Por favor ingrese un número entre 1 y {num_cartas}")
        except ValueError:
            print("Por favor ingrese un número válido")

def jugar_ronda(
    cartas_jugador: list, cartas_oponente: list, 
    tipo_oponente: str, nombre_jugador: str, ronda: int) -> dict:
    """
    Maneja la lógica de una ronda de juego.
    
    Args:
        cartas_jugador: Lista de cartas del jugador
        cartas_oponente: Lista de cartas del oponente
        tipo_oponente: Tipo de oponente ('aleatorio' o 'estrategico')
        nombre_jugador: Nombre del jugador
        ronda: Número de ronda actual
        
    Returns:
        dict: Información de la ronda jugada
    """
    print(f"\nRonda {ronda}")
    cartas_mostrar = []
    for c in cartas_jugador:
        carta_texto = f"{c['valor']} de {c['palo']}"
        cartas_mostrar.append(carta_texto)
    print("Cartas del jugador:", cartas_mostrar)
    
    #carta_jugador = int(input("Seleccione la carta a jugar (1, 2, 3): ")) - 1
    carta_jugador = obtener_carta_valida(len(cartas_jugador))
    carta_jugada_jugador = cartas_jugador.pop(carta_jugador)
    print(f"El jugador juega: {carta_jugada_jugador['valor']} de {carta_jugada_jugador['palo']}")

    if tipo_oponente == "aleatorio":
        carta_jugada_oponente = jugador_aleatorio(cartas_oponente, 0)
    else:
        carta_jugada_oponente = jugador_estrategico(cartas_oponente, 0, carta_jugada_jugador)

    cartas_oponente.remove(carta_jugada_oponente)
    print(f"El oponente juega: {carta_jugada_oponente['valor']} de {carta_jugada_oponente['palo']}")

    # Determinar ganador
    if carta_jugada_jugador["jerarquia"] > carta_jugada_oponente["jerarquia"]:
        ganador = nombre_jugador
        print(f"¡{nombre_jugador} gana la ronda!")
    else:
        ganador = tipo_oponente
        print(f"¡{tipo_oponente} gana la ronda!")

    return {
        "ronda": ronda,
        "ganador": ganador,
        "carta_jugador": f"{carta_jugada_jugador['valor']} de {carta_jugada_jugador['palo']}",
        "carta_oponente": f"{carta_jugada_oponente['valor']} de {carta_jugada_oponente['palo']}"
    }

def mostrar_estado_partida(
    nombre_jugador: str, tipo_oponente: str, puntos_jugador: int, 
    puntos_oponente: int, puntos_maximos: int) -> None:
    """
    Muestra el estado actual de la partida.
    
    Args:
        nombre_jugador: Nombre del jugador
        tipo_oponente: Tipo de oponente
        puntos_jugador: Puntos actuales del jugador
        puntos_oponente: Puntos actuales del oponente
        puntos_maximos: Puntos necesarios para ganar
    """
    puntos_restantes_jugador = puntos_maximos - puntos_jugador
    puntos_restantes_oponente = puntos_maximos - puntos_oponente
    print(f"\nPuntaje actual - {nombre_jugador}: {puntos_jugador}, {tipo_oponente}: {puntos_oponente}")
    print(f"Puntos para ganar - {nombre_jugador}: {puntos_restantes_jugador}, {tipo_oponente}: {puntos_restantes_oponente}")


def calcular_envido(cartas):
    """Calcula puntos de envido según las cartas"""
    # Agrupar cartas por palo
    palos = {}
    for carta in cartas:
        if carta['palo'] not in palos:
            palos[carta['palo']] = []
        palos[carta['palo']].append(carta['valor'])
    
    # Calcular puntos máximos
    max_puntos = 0
    for _, valores in palos.items():
        if len(valores) >= 2:
            puntos = 20 + sum(min(valor, 7) for valor in valores[:2])
            max_puntos = max(max_puntos, puntos)
    return max_puntos

def jugar_partida(nombre_jugador: str, tipo_oponente: str, puntos_maximos: int) -> dict:
    """
    Gestiona una partida completa de Truco usando las funciones refactorizadas.
    
    Args:
        nombre_jugador: Nombre del jugador
        tipo_oponente: Tipo de oponente ('aleatorio' o 'estrategico')
        puntos_maximos: Puntos necesarios para ganar
        
    Returns:
        dict: Resultado final de la partida
    """
    mazo = generar_mazo()
    puntos_jugador = 0
    puntos_oponente = 0
    historial_rondas = []

    while puntos_jugador < puntos_maximos and puntos_oponente < puntos_maximos:
        cartas_jugador, cartas_oponente = repartir_cartas(mazo)
        
        # Manejo del envido
        envido_jugador = calcular_envido(cartas_jugador)
        envido_oponente = calcular_envido(cartas_oponente)
        puntos_envido = manejar_envido(tipo_oponente, envido_jugador, envido_oponente)
        puntos_jugador += puntos_envido[0]
        puntos_oponente += puntos_envido[1]

        print("\n--- Inicio de nueva mano ---")
        victorias_jugador = 0
        victorias_oponente = 0

        # Jugar las 3 rondas
        for ronda in range(1, 4):
            resultado_ronda = jugar_ronda(cartas_jugador, cartas_oponente, tipo_oponente, nombre_jugador, ronda)
            historial_rondas.append(resultado_ronda)
            if resultado_ronda["ganador"] == nombre_jugador:
                victorias_jugador += 1
            else:
                victorias_oponente += 1

        # Determinar ganador de la mano
        if victorias_jugador > victorias_oponente:
            puntos_jugador += 1
            print(f"\n¡{nombre_jugador} gana la mano!")
        else:
            puntos_oponente += 1
            print(f"\n¡{tipo_oponente} gana la mano!")

        mostrar_estado_partida(nombre_jugador, tipo_oponente, puntos_jugador, puntos_oponente, puntos_maximos)

    resultado = {
        "jugador": nombre_jugador,
        "oponente": tipo_oponente,
        "puntos_jugador": puntos_jugador,
        "puntos_oponente": puntos_oponente,
        "historial_rondas": historial_rondas
    }

    guardar_historial(resultado)
    return resultado
