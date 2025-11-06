# Diseñar una clase Python llamada “Producto” con los atributos nombre, categoría,
# precio y cantidad. Diseña en esta clase el método __str__ de forma que retorne todos
# los atributos en un dato de tipo cadena (str).
# Crear dos productos pertenecientes a esa clase y mostrar todos los datos de aquel
# producto que tenga mayor precio.
from clases import Producto


producto1= Producto("PSP","videoconsola",175.99,500)
producto2= Producto("PS2","videoconsola",189.99,300)

Producto.mas_caro(producto1,producto2)