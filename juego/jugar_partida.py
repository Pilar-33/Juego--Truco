from juego.juego import*
from juego.cartas import*
from juego.estrategias import*
from juego.historial import*
import random
import csv

def jugar_ronda(cartas_jugador: list, cartas_oponente: list, tipo_oponente: str) -> tuple:
    print("\nTus cartas disponibles:")
    for i, carta in enumerate(cartas_jugador, 1):
        print(f"{i}. {carta['valor']} de {carta['palo']}")
    
    # Turno jugador
    indice = int(input("\nElige una carta (número): ")) - 1
    carta_jugador = cartas_jugador.pop(indice)
    
    # Turno oponente
    if tipo_oponente == "aleatorio":
        carta_oponente = random.choice(cartas_oponente)
    else:
        carta_oponente = max(cartas_oponente, key=lambda x: x["jerarquia"])
    cartas_oponente.remove(carta_oponente)
    
    print(f"\nJugaste: {carta_jugador['valor']} de {carta_jugador['palo']}")
    print(f"Oponente jugó: {carta_oponente['valor']} de {carta_oponente['palo']}")
    
    return carta_jugador, carta_oponente

def resolver_envido(envido_jugador: int, envido_oponente: int, tipo_oponente: str) -> tuple:
    print(f"\nTus puntos de envido: {envido_jugador}")
    quiere_cantar = input("¿Quieres cantar envido? (si/no): ").lower()
    
    if quiere_cantar == "si":
        if tipo_oponente == "aleatorio":
            acepta = random.choice([True, False])
        else:
            acepta = envido_oponente >= 25
            
        if acepta:
            print("\nOponente acepta el envido")
            if envido_jugador > envido_oponente:
                return 2, 0
            else:
                return 0, 2
        else:
            print("\nOponente no quiere el envido")
            return 1, 0
    return 0, 0

def jugar_partida(
    nombre_jugador: str, tipo_oponente: str, 
    max_puntos: int) -> None:
    puntos_jugador = 0
    puntos_oponente = 0
    
    while puntos_jugador < max_puntos and puntos_oponente < max_puntos:
        # Preparar ronda
        mazo = generar_mazo(VALORES, PALOS)
        cartas_jugador, cartas_oponente = repartir_cartas(mazo)
        
        # Mostrar cartas iniciales
        print("\nTus cartas:")
        for carta in cartas_jugador:
            print(f"{carta['valor']} de {carta['palo']}")
            
        # Fase envido
        envido_jugador = calcular_envido(cartas_jugador)
        envido_oponente = calcular_envido(cartas_oponente)
        puntos_env_j, puntos_env_o = resolver_envido(envido_jugador, envido_oponente, tipo_oponente)
        puntos_jugador += puntos_env_j
        puntos_oponente += puntos_env_o
        
        # Fase juego
        cartas_j = cartas_jugador.copy()
        cartas_o = cartas_oponente.copy()
        
        for i in range(3):
            print(f"\nRonda {i+1}")
            carta_j, carta_o = jugar_ronda(cartas_j, cartas_o, tipo_oponente)
            
            if carta_j["jerarquia"] > carta_o["jerarquia"]:
                puntos_jugador += 1
                print("¡Ganaste la ronda!")
            else:
                puntos_oponente += 1
                print("¡Perdiste la ronda!")
                
        print(f"\nPuntaje - {nombre_jugador}: {puntos_jugador}, Oponente: {puntos_oponente}")
    
    # Guardar resultado
    with open("historial.csv", "a", newline="") as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre_jugador, tipo_oponente, puntos_jugador, puntos_oponente])
    
    if puntos_jugador >= max_puntos:
        print(f"\n¡Felicitaciones {nombre_jugador}! ¡Ganaste la partida!")
    else:
        print("\n¡El oponente ganó la partida!")