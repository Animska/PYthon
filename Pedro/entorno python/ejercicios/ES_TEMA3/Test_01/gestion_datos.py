"""Gestión de personas y eventos."""

from typing import Dict, Set, Tuple, List, Optional
import doctest

eventos: Dict[str, Set[int]] = {}
personas: Dict[int, Tuple[str, str, str]] = {}


def agregar_persona(
    dict_personas: Dict[int, Tuple[str, str, str]],
    nombre: str,
    apellido: str,
    telefono: str,
) -> bool:
    """
    Agrega una persona al diccionario dict_personas.

    :param dict_personas: Diccionario de personas.
    :param nombre: Nombre de la persona que desea agregar.
    :param apellido: Apellido de la persona que desea agregar.
    :param telefono: Teléfono de la persona que desea agregar.

    >>> agregar_persona(personas, "Sergio", "Guerrero", "+34111222333")
    Este usuario ya existe
    False
    """
    tupla_persona = (nombre, apellido, telefono)
    if tupla_persona in dict_personas.values():
        print("Este usuario ya existe")
        return False

    if not dict_personas:
        dict_personas[1111] = tupla_persona
        print("Persona añadida satisfactoriamente")
        return True
    else:
        ultima_clave = max(dict_personas.keys())
        dict_personas[ultima_clave + 1] = tupla_persona
        print("Persona añadida satisfactoriamente")
        return True

def obtener_persona(
    dict_personas: Dict[int, Tuple[str, str, str]],
    persona_id: int,
) -> Optional[Tuple[str, str, str]]:
    """
    Obtiene los datos de una persona por su id.

    :param dict_personas: Diccionario de personas.
    :param persona_id: El id y clave en el diccionario personas.
    :return: Tupla con los datos de la persona o None si no existe.

    >>> obtener_persona({1111: ("Sergio", "Guerrero", "+34111222333")}, 1111)
    ('Sergio', 'Guerrero', '+34111222333')
    """
    return dict_personas.get(persona_id)

def buscar_persona(
    dict_personas: Dict[int, Tuple[str, str, str]],
    nombre: str,
    apellidos: str,
) -> Optional[int]:
    """
    Busca una persona según su nombre y apellidos.

    :param dict_personas: Diccionario de personas.
    :param nombre: Nombre de la persona que buscas.
    :param apellidos: Apellidos de la persona que buscas.
    :return: Id de la persona o None si no se encuentra.

    >>> buscar_persona(personas, "Sergio", "Guerrero")
    1111
    """
    for id_persona, datos in dict_personas.items():
        if datos[0] == nombre and datos[1] == apellidos:
            return id_persona
    return None


def agregar_evento(
    dict_eventos: Dict[str, Set[int]],
    nombre_evento: str,
) -> bool:
    """
    Agrega un evento al diccionario de eventos.

    :param dict_eventos: Diccionario de eventos.
    :param nombre_evento: Nombre del evento que vas a agregar.
    :return: True si se ha añadido el evento, False si ya existía.
    """
    if nombre_evento not in dict_eventos:
        dict_eventos[nombre_evento] = set()
        return True
    return False


def agregar_participante(
    dict_eventos: Dict[str, Set[int]],
    dict_personas: Dict[int, Tuple[str, str, str]],
    nombre_evento: str,
    id_participante: int,
) -> bool:
    """
    Agrega un participante a un evento.

    :param dict_eventos: Diccionario de eventos.
    :param dict_personas: Diccionario de personas.
    :param nombre_evento: Nombre del evento.
    :param id_participante: Id del participante.
    :return: True si se ha añadido el participante al evento, False en caso contrario.
    """
    if nombre_evento in dict_eventos and id_participante in dict_personas:
        dict_eventos[nombre_evento].add(id_participante)
        print("Participante añadido satisfactoriamente")
        return True
    return False


def eventos_comunes(
    dict_eventos: Dict[str, Set[int]],
    id_participantes: List[int],
) -> Tuple[str, ...]:
    """
    Devuelve los eventos a los que han asistido todos los ids de la lista.

    :param dict_eventos: Diccionario de eventos.
    :param id_participantes: Lista de ids de personas.
    :return: Tupla con los nombres de eventos comunes.
    """
    comunes: Set[str] = set()
    set_ids = set(id_participantes)

    for evento, participantes in dict_eventos.items():
        if set_ids.issubset(participantes):
            comunes.add(evento)

    return tuple(comunes)


def evento_mayor(dict_eventos: Dict[str, Set[int]]) -> Tuple[str, int] | Tuple[()]:
    """
    Devuelve el evento con mayor número de participantes.

    :param dict_eventos: Diccionario de eventos.
    :return: Tupla (nombre_evento, num_participantes) o tupla vacía si no hay eventos.
    """
    if not dict_eventos:
        return tuple()
    evento_max = max(dict_eventos, key=lambda k: len(dict_eventos[k]))
    return evento_max, len(dict_eventos[evento_max])


if __name__ == "__main__":
    # 1. Agregar personas
    agregar_persona(personas, "Sergio", "Guerrero", "+34111222333")
    agregar_persona(personas, "Ana", "López", "+34222333444")
    print(personas)

    # 2. Probar funciones de persona
    print(obtener_persona(personas, 1111))
    print(buscar_persona(personas, "Sergio", "Guerrero"))

    # 3. Crear eventos
    agregar_evento(eventos, "Cumpleaños")
    agregar_evento(eventos, "Concierto")
    print(eventos)

    # 4. Agregar participantes
    agregar_participante(eventos, personas, "Cumpleaños", 1111)
    agregar_participante(eventos, personas, "Cumpleaños", 1112)
    agregar_participante(eventos, personas, "Concierto", 1111)
    print(eventos)

    # 5. Evento con más participantes
    print(evento_mayor(eventos))

    # 6. Eventos comunes
    print(eventos_comunes(eventos, [1111]))
    print(eventos_comunes(eventos, [1111, 1112]))
    print(eventos_comunes(eventos, [1112, 1111]))

    doctest.testmod()
