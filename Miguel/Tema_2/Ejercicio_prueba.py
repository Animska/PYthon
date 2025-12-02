# Ejercicio 5_1:
# Crea una función llamada validar_entradas(lista_entradas) que procese la siguiente
# lista y devuelva una tupla (Nombre de Campo, Valor, ¿Es Válido?) para cada entrada
# según estas reglas:
# - Código de Producto: Debe ser alfanumérico (isalnum()) y tener exactamente 5
# caracteres.
# - Nombre de Usuario: Debe ser estrictamente alfabético (isalpha()).
# - PIN: Debe ser estrictamente numérico (isdigit()) y tener exactamente 4 caracteres

def validar_entradas(lista_entradas: list):
    """
    Docstring para validar_entradas
    
    :param lista_entradas: Descripción
    :type lista_entradas: list
    """
    resultados=[]
    for entrada in lista_entradas:
        match entrada[0]:
            case 'CodigoProducto':
                if entrada[1].isalnum() and len(entrada[1]) == 5:
                    resultados.append((entrada[0],entrada[1],True))
                else:
                    resultados.append((entrada[0],entrada[1],False))
            
            case 'NombreUsuario':
                if entrada[1].isalpha():
                    resultados.append((entrada[0],entrada[1],True))
                else:
                    resultados.append((entrada[0],entrada[1],False))

            case 'PIN':
                if entrada[1].isdigit() and len(entrada[1]) == 4:
                    resultados.append((entrada[0],entrada[1],True))
                else:
                    resultados.append((entrada[0],entrada[1],False))


    return resultados

# Datos de prueba
entradas_a_validar = [
("CodigoProducto", "P001A"), # Válido
("CodigoProducto", "P-001"), # Inválido (contiene '-')
("NombreUsuario", "AnaLopez"), # Válido
("NombreUsuario", "AnaLopez1"), # Inválido (contiene '1')
("PIN", "1234"), # Válido
("PIN", "123a"), # Inválido (contiene 'a')
("PIN", "123"), # Inválido (longitud incorrecta)
]
# Procesar y mostrar resultados
resultados_validos = validar_entradas(entradas_a_validar)
print("--- Validación de Entradas ---")
for campo, valor, es_valido in resultados_validos:
    estado = "VÁLIDO" if es_valido else "INVÁLIDO"
    print(f"[{campo}] -> '{valor}' : {estado}")