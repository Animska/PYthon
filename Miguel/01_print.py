# estaEsUnaVariable = camel case
# esta_es_una_variable = snake case
# esta-es-una-variable = kebab case

# print("hola mundo otra vez")

# if True:
#     print("ooooooooo")

# variable = "tre"
# print(variable)

# nombre="Sergio"
# edad=24
# print("Mi nombre es :"+nombre+" y tengo "+str(edad)+" años.")

# print(f"El año que viene tendre {edad+1} años")

# nombre= "sergio Guerrero"
# print(nombre.title())
# print(nombre.upper())
# print(nombre.lower())

# print("Python")
# print("\tPython")
# print("Lenguaje \nPython"

# var="             Lenguaje      Python           "
# print(len(var.lstrip()))

# var="eeeeeeeeeeeeeeeeeeeeeeeeeeeaaaaaaaaaaaaaaaaaaaaaaaaa"
# var_striped=var.strip("a")
# print(var_striped)

# url="http://suarezdefigueroa.es:8080/?redirect=0"
# print(url.removeprefix("http://"))
# print(url.removesuffix("/?redirect=0"))

# Pide la edad del usuario y muestra un mensaje segun su rango de edad
# -menor de 12= eres un niño
# -entre 12 y 17 eres un adolescente
# -entre 18 y 64 eres un adulto
# -mayor de 65 eres un jubilado

# edad=int(input('introduzca su edad\n'))
# if edad<12:
#     print("eres un niño")
# elif edad>=12 and edad <=17:
#     print("eres un adolescente")
# elif edad>=18 and edad <=64:
#     print("eres un adulto")
# elif edad >=65:
#     print("eres un jubilado")
# else:
#     print("dato incorrecto introducido")


# for i in range(5):
#     print(i)

# que pida un numero y muestre su tabla de multiplicar del 1 al 10

# num=int(input("introduzca el numero que quieras ver la tabla de multiplicar\n"))
# for i in range(1,11):
#     print(f"{num} X {i}:{num*i}")

# coches=["Mclaren","Ferrari","Toyota"]

# for coche in coches:
#     print(coche)


# cont=1
# while cont<=5:
#     print("a")
#     cont+=1


# """
# Elige un numero secreto entre 1 y 10
# el usuario debe adivinarlo y el programa dira si ha acertado
# """

# import random

# num_secreto = random.randint(1,10)
# numero=0
# while numero != num_secreto:
#     numero=int(input("introduce el numero secreto: "))
#     if numero>num_secreto:
#         print("te has pasao")
#     elif numero<num_secreto:
#         print("te has quedao corto")

# print("has ganado")

# """
# Pide una palabra al usuario y muestra cuantas letras tiene pero sin contar las vocales
# """

# palabra=input("introduzca una palabra : ")
# cont=0
# for letra in palabra:
#     if letra in "aeiouAEIOU":
#         continue
#     cont+=1
#     print(letra,end=" ")
# print(f"\ncontiene {cont} letras sin contar vocales")

# print(f"El precio completo es:{15.5765:.2f}")

#imprime sin tener en cuenta \n o \t
# print(r"C:\documentos\nombres")

# Devuelve false si es 0, 0.0, "" o None
# numero=" "
# if numero:
#     print("a")
# else:
#     print("o")


# frase = "Python es divertido"
# print("Python" in frase) # True
# print("python" in frase) # False (distingue mayúsculas/minúsculas)
# print("diver" in frase) # True (aparece dentro de la palabra)
# print("Java" not in frase) # True

# colores = ["rojo", "verde", "azul"]
# print("rojo" in colores) # True
# print("negro" in colores) # False
# print("amarillo" not in colores) # True


# animales = ["perro", "gato", "pez", "loro", "canario", "hamster", "tortuga"]
# animales_mayusculas = [animal.upper() for animal in animales]
# print(animales_mayusculas)

# pares = [num for num in [1,2,3,4,5,6] if num % 2 == 0]
# print(pares)

# linea = input("Escribe algo: ")
# while linea != "salir":
#     print("Has escrito:", linea)
#     linea = input("Escribe algo: ")

# while (linea := input("Escribe algo: ")) != "salir":
#     print("Has escrito:", linea)

# """
# Ejemplo de uso en un while:
# """
# secreto = random.randint(1, 10)
# while (intento := int(input("Adivina el número (1–10): "))) != secreto:
#     if intento < secreto:
#         print("Demasiado bajo.")
#     else:
#         print("Demasiado alto.")
# print("¡Correcto!")

# """
# Ejemplo de uso en un if:
# """
# if (nombre := input("Introduce tu nombre: ")):
#     print(f"Hola, {nombre}!")
# else:
#     print("No has escrito nada.")


# Para evitarlo, Python ofrece el bloque try...except.
# try:
# # Código que podría causar un error
# except:
# # Código que se ejecuta si ocurre un error

# Ejemplo para controlar un error simple:
# try:
#     numero = int(input("Introduce un número: "))
#     print(f"El doble es: {numero * 2}")
# except:
#     print("Debes introducir un número válido.")

# Ejemplo capturando tipos de error
# try:
#     a = int(input("Introduce el primer número: "))
#     b = int(input("Introduce el segundo número: "))
#     print(a / b)
# except ValueError:
#     print("Debes introducir solo números.")
# except ZeroDivisionError:
#     print("No puedes dividir entre cero.")
