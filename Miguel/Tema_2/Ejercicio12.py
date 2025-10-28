# Ejercicio 12
# Crear una función sumaproducto que reciba por parámetro
# - Operación: una cadena que indica si se realiza la suma o el producto.
# - Un número variable de parámetros que se considerarán como números. Estos
# parámetros serán los operandos.
# La función devuelve la suma o el producto de todos los números recibidos por
# parámetros. Si la operación no es ni "suma" ni "producto" se imprime un mensaje de
# error y devuelve None.

def sumaproducto(operacion,*args):
    match operacion:
        case "suma":
            suma = 0
            for numero in args:
                suma += numero
            return suma
        case "producto":
            producto = 1
            for numero in args:
                producto *= numero
            return producto
        case _:
            print("error")
            return None
        
print(sumaproducto("suma",1,2,3,4,5))
print(sumaproducto("producto",1,2,3,4,5))
print(sumaproducto("wiwo",1,2,3,4,5))