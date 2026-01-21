def agregar_jugador(goleadores:dict, jugador:str, equipo:str, posicion:str, goles:int)->bool:
    """
    Funcion que agrega un jugador al diccionario goleadores
    -------------------------------------------------------
    Args:
        -goleadores: diccionario de los goleadores
        -jugador: nombre del jugador
        -equipo: nombre del equipo donde esta el jugador
        -posicion: posicion del jugador en el equipo
        -goles: numero de goles que ha marcado el jugador
    """
    if goleadores and jugador and equipo and posicion and goles:
        if jugador not in goleadores.keys():
            goleadores[jugador] = (equipo, posicion, goles)
            return True
    
    return False

def actualizar_goles(goleadores:dict,jugador:str,goles:int)->bool:
    """
    Funcion para cambiar el numero de goles de un jugador
    -----------------------------------------------------
    Args:
        -goleadores: diccionario de los goleadores
        -jugador: nombre del jugador
        -goles: numero de goles por los que se reemplazaran los del jugador
    """
    if goleadores and jugador and goles>=1:
        if jugador in goleadores.keys():
            nueva_tupla = (goleadores[jugador][0],goleadores[jugador][1],goles)
            goleadores[jugador] = nueva_tupla
            return True
        
    return False

def max_goles_pos(goleadores:dict, posicion:str)->bool:
    """
    Funcion para buscar a los jugadores con mas goles de una posicion concreta
    -----------------------------------------------------
    Args:
        -goleadores: diccionario de los goleadores
        -posicion: posicion donde se buscara el jugador
    """
    if not goleadores:
        return tuple()
    
    lista_goleadores=list()
    max_goles=0
    for datos in goleadores.values():
        if datos[2]>max_goles and datos[1].lower() == posicion.lower():
            max_goles = datos[2]
            
    if max_goles <= 0:
        return tuple()

    lista_goleadores.append(max_goles)
    for jugador,datos in goleadores.items():
        if datos[2] == max_goles and datos[1].lower() == posicion.lower():
            lista_goleadores.append(jugador)

    return tuple(lista_goleadores)

def max_goleadores(goleadores:dict)->dict:
    """
    Funcion para buscar los maximos goleadores por cada posicion
    -----------------------------------------------------
    Args:
        -goleadores: diccionario de los goleadores
    """
    if not goleadores:
        return dict()
    
    posiciones=set()
    for datos in goleadores.values():
        posiciones.add(datos[1])

    dict_posiciones = dict()
    for posicion in posiciones:
        dict_posiciones[posicion] = max_goles_pos(goleadores, posicion)

    return dict_posiciones

def mostrar_jugadores_por_equipo(goleadores:dict)->None:
    """
    Funcion para mostrar todos los datos de los jugadores ordenados
    alfabeticamente segun su equipo
    ---------------------------------------------------------------
    Args:
        -goleadores: diccionario de los goleadores
    """
    jugadores_ordenado = sorted(goleadores, key=lambda k: goleadores[k][0])
    #esto devuelve una lista de los jugadores ordenados segun el nombre de su equipo
    print("-"*60)
    print(f"|{'JUGADOR':^20}|{'EQUIPO':^20}|{'POSICION':^10}|{'GOLES':^5}|")
    print("-"*60)
    for jugador in jugadores_ordenado:
        equipo,posicion,goles = goleadores.get(jugador)
        print(f"|{jugador:<20}|{equipo:<20}|{posicion:<10}|{goles:^5}|")

#------------------------------------------------------------
def main():
    jugadores = {
    "Valverde": ("Real Madrid","Medio", 5),
    "Mbappe": ("Real Madrid","Delantero", 22),
    "Raphinha": ("Barcelona","Extremo", 13),
    "Lwewandowski": ("Barcelona","Delantero", 25),
    "Vinicius": ("Real Madrid","Extremo", 13),
    "Griezmann": ("Atletico Madrdid","Delantero", 6)
    }

    print(f"{'--EXAMEN ESTRUCTURAS Y SINTAXIS TEMA 2--':^60}")
    #Ejercicio 01.-
    #Ejemplo correcto
    if agregar_jugador(jugadores, 'Axel Blaze', 'Raimon', 'Delantero', 115):
        print('Jugador agregado satisfactoriamente!')
    else:
        print("ERROR")

    print()
    #Ejemplo incorrecto
    if agregar_jugador(jugadores, 'Axel Blaze', 'Raimon', 'Delantero', 115):
        print('jugador agregado satisfactoriamente!')
    else:
        print("ERROR")
    print("-"*60)
    print()
    
    #Ejercicio 02.-
    #Ejemplo correcto
    if actualizar_goles(jugadores, 'Axel Blaze', 145):
        print('Cambio a los goles realizado satisfactoriamente!')
    else:
        print("ERROR")

    print()
    #Ejemplo incorrecto
    if actualizar_goles(jugadores, 'Ael Blaze', 145):
        print('Cambio a los goles realizado satisfactoriamente!')
    else:
        print("ERROR")

    print("-"*60)
    print()

    #Ejercicio 03.-
    #Ejemplo correcto
    print(max_goles_pos(jugadores, 'Delantero'))

    print()
    #Ejemplo incorrecto
    print(max_goles_pos(jugadores, 'wiwiwi'))

    print("-"*60)
    print()
    
    #Ejercicio 04.-
    dict_goleadores=max_goleadores(jugadores)
    print(f"{'POSICION':^10}|{'GOLES':^7}|{'JUGADORES'}")
    for posicion, jugadores_posicion in dict_goleadores.items():
        goles,*jugadores_max_goles = jugadores_posicion
        print(f"{posicion:<10}|{goles:^7}|{jugadores_max_goles}")
    print("-"*60)
    print()

    #Ejercicio 05.-
    mostrar_jugadores_por_equipo(jugadores)
    print("-"*60)
    print()

if __name__ == "__main__":
    main()