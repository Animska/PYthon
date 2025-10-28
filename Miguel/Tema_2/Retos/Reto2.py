# Escribe una función en Python que reciba una lista de números enteros y devuelva la
# suma total de los huevos que pertenecen a los dinosaurios carnívoros (es decir, la suma
# de todos los números pares en la lista).

huevos=[1,5,3,6,8,5,9,3,2,7,1,7,8]

def huevos_carnivoros(lista_huevos):
    pares = sum([num for num in lista_huevos if num%2==0])
    return pares

print("""
¿Cuantos huevos de carnivoros hay en el parque \n 
a pesar de que los dinosaurios de jurassic park \n 
estan modificados geneticamentes para ser todos hembras\n 
aunque eso pasa luego en un entorno descontrolado \n 
y no deberia pasar de normal en el parque?")
    """
    )
print(huevos_carnivoros(huevos))