from Producto import Producto

from Trazabilidad import Trazabilidad

# --- ZONA DE PRUEBA ---

print("### INICIO DE LA GESTIÓN DE LOTES ###")

# 1. Creación y validación exitosa
try:
    p1 = Producto("Paracetamol", "LOTE-P45") # Lote válido
    p2 = Producto("Paracetamol", "LOTE-P46") # Lote válido
    p3 = Producto("Paracetamol", "LOTE-P47") # Lote válido
    p4 = Producto("Amoxicilina", "LOTE-A10") # Lote válido
    p5 = Producto("Amoxicilina", "LOTE-A11") # Lote válido
    p6 = Producto("Amoxicilina", "LOTE-A12") # Lote válido
    p7 = Producto("Paracetamol", "LOTE-X99") # Lote válido, incrementa stock
    p8 = Producto("Paracetamol", "LOTE-Z01") # Lote válido, incrementa stock
except ValueError as e:
    print(f"Error al crear producto válido: {e}")

Trazabilidad.consultar_stock_total(Producto.STOCK_TOTAL)

# 2. Intento de creación con lote inválido (Debe fallar)
try:
    p_invalido_long = Producto("Vitamina C", "LOTE") # Longitud incorrecta
except ValueError as e:
    print(f"\nExcepción esperada (Longitud): {e}")

try:
    p_invalido_prefijo = Producto("Aspirina", "XOTE-A22") # Prefijo incorrecto
except ValueError as e:
    print(f"\nExcepción esperada (Prefijo): {e}")


# 3. Simulación de ventas
print("\n--- Simulación de Ventas ---")
p1.vender() # Vender Paracetamol (Stock 2 -> 1)
p1.vender() # Vender Paracetamol (Stock 1 -> 0)

# 4. Intento de venta de stock agotado (Debe fallar)
try:
    p1.vender() # Vender Paracetamol (Stock 0 -> Error)
except RuntimeError as e:
    print(f"\nExcepción esperada (Stock agotado): {e}")
    
Trazabilidad.consultar_stock_total(Producto.STOCK_TOTAL)
Trazabilidad.generar_reporte_bajo_stock(Producto.STOCK_TOTAL,1)
print(Trazabilidad.listar_nombres_disponibles(Producto.STOCK_TOTAL))