DATOS_SUCIOS = [
    "Juan", "Maria", "juan", None, "Ana", 
    "Maria", "Luis", "Ana", "PEDRO", None, 
    "luis", "ana", "Juan"
]

def analizar_datos(data: list) -> tuple:
    lista_limpia = [a.upper() for a in data if a is not None]
    conjunto_unicos = set(lista_limpia)
    # Total original y total únicos para cálculo de porcentaje duplicados
    total_original = len(lista_limpia)
    total_unicos = len(conjunto_unicos)
    porcentaje_duplicados = ((total_original - total_unicos) / total_original) * 100 if total_original > 0 else 0
    return (lista_limpia, conjunto_unicos, porcentaje_duplicados)

# Prueba
normalizados, unicos, porcentaje = analizar_datos(DATOS_SUCIOS)

print(f"Datos Normalizados: {normalizados}")
print(f"Elementos Únicos (Set): {unicos}")
print(f"Porcentaje de duplicados: {porcentaje:.2f}%") # (5 duplicados / 12 elementos limpios)