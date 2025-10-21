numero=int(input("introduce un numero para mostrar su tabla de multiplicar"))
print(f"tabla de multiplicar del {numero}:")
for i in range(1,11):
    print(f"{numero} x {i} = {numero*i}")