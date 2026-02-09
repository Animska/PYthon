import inventario
import pytest

# Esta fixture se ejecuta antes de cada test para asegurar un entorno limpio
@pytest.fixture(autouse=True)
def clean_inventario():
    inventario.inventario.clear()

#-------agregar_producto-----------
@pytest.mark.parametrize("a, b, c, resultado", [
    ('cosa1', 10.00, 15, True),
    ('cosa1', 9.99, 14, False)
])
def test_agregar_producto(a, b, c, resultado):
    # Para el caso False, debemos asegurar que ya exista
    if resultado is False:
        inventario.agregar_producto(a, b, c)
    assert inventario.agregar_producto(a, b, c) == resultado

#-------get_producto-----------
@pytest.mark.parametrize("nombre, esperado", [
    ('cosa1', (10.99, 15)),
    ('cosa300', (0, 0))
])
def test_get_producto(nombre, esperado):
    if nombre == 'cosa1':
        inventario.agregar_producto('cosa1', 10.99, 15)
    assert inventario.get_producto(nombre) == esperado

#-------actualizar_stock-----------
def test_actualizar_stock():
    inventario.agregar_producto("item", 5.0, 10)
    # Caso éxito
    assert inventario.actualizar_stock("item", 50) is True
    assert inventario.get_producto("item")[1] == 50
    # Caso falla (no existe)
    assert inventario.actualizar_stock("inexistente", 10) is False

#-------eliminar_producto-----------
def test_eliminar_producto():
    inventario.agregar_producto("borrar", 1.0, 1)
    assert inventario.eliminar_producto("borrar") is True
    assert inventario.eliminar_producto("borrar") is False # Ya no existe

#-------calcular_valor-----------
def test_calcular_valor():
    inventario.agregar_producto("A", 10.0, 2) # 20.0
    inventario.agregar_producto("B", 5.0, 4)  # 20.0
    assert inventario.calcular_valor() == 40.0

#-------return_dict-----------
def test_return_dict():
    inventario.agregar_producto("A", 1.0, 1)
    dic = inventario.return_dict()
    assert isinstance(dic, dict)
    assert "A" in dic