# Tienes una lista de pedidos de clientes, donde cada pedido es una tupla (cantidad,
# precio_unitario, estado).
# - Filtrar (filter): Obtén solo los pedidos que están en estado 'ENVIADO'.
# - Mapear (map): Calcula el coste total de cada pedido restante (cantidad ×
# precio_unitario).
# - Reducir (reduce): Suma todos los costes totales para obtener el ingreso bruto total de
# los pedidos enviado
from functools import reduce


pedidos = [
    (5, 10.0, 'ENVIADO'),
    (10, 2.5, 'PENDIENTE'),
    (2, 50.0, 'ENVIADO'),
    (3, 30.0, 'CANCELADO'),
    (1, 15.0, 'ENVIADO')
]

# 1. Filtrar
pedidos_enviados = list(filter(lambda p: p[2] == 'ENVIADO', pedidos))

# 2. Mapear
costes = list(map(lambda p: p[0] * p[1], pedidos_enviados))

# 3. Reduce
ingreso_bruto = reduce(lambda acc, x: acc + x, costes)

print(ingreso_bruto)