# Ejercicio 1
# Lea dos números enteros que serán los operandos de la operación (operando1 y
# operando2).
# Lea un tercer número que identificará la operación.
# Si operación es 0 calcula la suma de ambos operandos y muestra el resultado.
# Si operación es 1 calcula la resta. 
# Si operación es 2 calcula la multiplicación.
# Si operación es 3 calcula la división.
# Si operación no coincide con ningún valor válido mostrará un mensaje de error

def calculadora(num1,num2,operacion):
    if operacion in range(0,3):
        match operacion:
            case 0:
                return num1+num2
            case 1:
                return num1-num2
            case 2:
                return num1*num2
            case 3:
                return num1/num2
            case _:
                return "la operacion no coindice vuelva a intentarlo"
try:            
    num1=int(input("introduzca un numero: "))
    num2=int(input("introduzca otro numero: "))
    operacion=int(input("""
    Introduzca la operacion:
        0.-suma
        1.-resta
        2.-multiplicacion
        3.-division
    """))
    print(f"El resultado es: {calculadora(num1,num2,operacion)}")
except ValueError:
    print("ERROR! tienes que introducir un numero")
except ZeroDivisionError:
    print("ERROR! no se puede dividir entre 0")