eventos = dict()
personas = dict()

def agregar_persona(dict_personas:dict,nombre:str,apellido:str,telefono:str):
    tupla_persona = (nombre, apellido, telefono)
    if tupla_persona in dict_personas.values():
        print("Este usuario ya existe")
        return
    
    if not dict_personas:
        dict_personas[1111] = tupla_persona
    else:
        ultima_clave = max(dict_personas.keys())
        dict_personas[ultima_clave + 1] = tupla_persona
    print('Persona añadida satisfactoriamente')

def obtener_persona(dict_personas:dict, id:int)->tuple:
    return dict_personas.get(id)

def buscar_persona(dict_personas:dict, nombre:str, apellidos:str)->int:
    for id_persona, datos in dict_personas.items():
        if datos[0] == nombre and datos[1] == apellidos:
            return id_persona
        
    return None

def agregar_evento(dict_eventos:dict,nombre_evento:str)->bool:
    if nombre_evento not in dict_eventos:
        dict_eventos[nombre_evento] = set()
        return True
    
    return False

def agregar_participante(dict_eventos:dict,dict_personas:dict,nombre_evento:str,id_participante:int)->bool:
    if nombre_evento in dict_eventos and id_participante in dict_personas:
        dict_eventos[nombre_evento].add(id_participante)
        print('Participante añadido satisfactoriamente')
        return True
    
    return False

def eventos_comunes(dict_eventos:dict, id_participantes:list)->tuple:
    comunes = set()
    set_ids = set(id_participantes)

    for evento,participantes in eventos.items():
        if set_ids.issubset(participantes):
            comunes.add(evento)
    
    return tuple(comunes)
    
    
    # if not id_participantes:
    #     return tuple()
    
    # eventos_comunes = set()
    # primer_id = id_participantes[0]
    # for evento_id, participantes in dict_eventos.items():
    #     if primer_id in participantes:
    #         eventos_comunes.add(evento_id)

    # if len(id_participantes) == 1:
    #     return tuple(eventos_comunes)
    
    # for id_participante in id_participantes[1:]:
    #     nuevos_comunes = set()
    #     for evento_id, participantes in dict_eventos.items():
    #         if id_participante in participantes and evento_id in eventos_comunes:
    #             nuevos_comunes.add(evento_id)
    #     eventos_comunes = nuevos_comunes
    #     if not eventos_comunes:
    #         return tuple()
    
    # return tuple(eventos_comunes)

def evento_mayor(dict_eventos:dict)->tuple:
    if not dict_eventos:
        return None
    evento_mayor = max(dict_eventos, key=lambda k: len(dict_eventos[k]))
    return (evento_mayor,len(dict_eventos[evento_mayor]))

#------------------------------------------------------------------------------------

# 1. Agregar personas
agregar_persona(personas,'Sergio','Guerrero','+34111222333')
agregar_persona(personas,'Ana','López','+34222333444')
print(personas)
# {'1111': ('Sergio', 'Guerrero', '+34111222333'), 
#  '1112': ('Ana', 'López', '+34222333444')}

# 2. Probar funciones de persona
print(obtener_persona(personas, 1111))  # ('Sergio', 'Guerrero', '+34111222333')
print(buscar_persona(personas,'Sergio', 'Guerrero'))  # 1111

# 3. Crear eventos
agregar_evento(eventos, "Cumpleaños")
agregar_evento(eventos, "Concierto")
print(eventos)  # {'Cumpleaños': set(), 'Concierto': set()}

# 4. Agregar participantes
agregar_participante(eventos, personas, "Cumpleaños", 1111)
agregar_participante(eventos, personas, "Cumpleaños", 1112)
agregar_participante(eventos, personas, "Concierto", 1111)
print(eventos)
# {'Cumpleaños': {1111, 1112}, 'Concierto': {1111}}

# 5. Evento con más participantes
print(evento_mayor(eventos))  # ()"Cumpleaños",2)

# 6. Eventos comunes
print(eventos_comunes(eventos, [1111]))  # ('Cumpleaños', 'Concierto')
print(eventos_comunes(eventos, [1111, 1112]))  # ('Cumpleaños',)
print(eventos_comunes(eventos, [1112, 1111]))  # ('Cumpleaños',)

