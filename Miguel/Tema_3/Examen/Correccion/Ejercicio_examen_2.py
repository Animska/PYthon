def  procesar_matriz(matriz_texto: list)->list:
    matriz=[]
    for elemento in matriz_texto:
        lista=[]
        for numero in elemento.split(','):
            lista.append(float(numero))
        matriz.append(lista)

    lista_filtrada=[lista for lista in matriz if lista[0]>10]
    print(f"""{matriz_texto} se transforma en:
    {matriz}""")
    return lista_filtrada

datos_matriz = [
    "5.1,1.0,2.5",
    "12.3,4.0,9.1",
    "9.9,8.0,3.0",
    "15.0,2.1,1.1"
]
try:
    matriz_filtrada = procesar_matriz(datos_matriz)
    print("Filas filtradas (Primer valor > 10.0):")
    for fila in matriz_filtrada: print(f"  {fila}")
    # Salida: [[12.3, 4.0, 9.1], [15.0, 2.1, 1.1]]
except ValueError as e:
    print(f"ERROR {e}")