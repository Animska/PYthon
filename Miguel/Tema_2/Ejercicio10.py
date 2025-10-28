# Dado un diccionario con notas de varios alumnos, muestra por pantalla los que han
# aprobado (nota mayor o igual a 5).
notas = {
"Ana": 8,
"Luis": 4,
"María": 6,
"Pedro": 3
}

aprobado={k:v for k,v in notas.items() if v>=5}
print(aprobado)