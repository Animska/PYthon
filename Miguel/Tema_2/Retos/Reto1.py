# Crea una función en Python que reciba una cadena de texto. Esta función debe contar
# cuántas veces aparece la letra R (para Reed Richards) y cuántas veces aparece la letra J
# (para Johnny Storm) en la cadena.
# - Si la cantidad de R y la cantidad de J son iguales, se considera que la alianza entre la
# mente y el fuego está en equilibrio y la función debe retornar True.
# - Si las cantidades no son iguales, la función debe retornar False.
# - En el caso de que no aparezca ninguna de las dos letras en la cadena, se entiende que
# el equilibrio se mantiene (0 = 0), por lo que la función debe retornar True.

def mrfantastico_vs_cuñado(texto):
    cont_r=texto.lower().count("r")
    cont_j=texto.lower().count("j")

    return cont_r==cont_j
    
print("¿Hay alianza entre Mr Fantastico y la Antorcha Humana?")
print(mrfantastico_vs_cuñado("JRJRJRJRJRJRJRJRJRjrjrjrjrjrjrjr"))