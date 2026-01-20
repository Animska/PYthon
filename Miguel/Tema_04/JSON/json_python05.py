# Ejercicio 5 - Validación de JSON
# Escribe una función validar_usuario(json_string) que:
# 1. Intente deserializar el JSON
# 2. Verificar que sea un diccionario
# 3. Verifique que existan las claves: nombre, email, edad
# 4. Verifique que edad sea un número entre 18 y 100
# 5. Verifique que email contenga el carácter '@
import json

def validar_usuario(json_string: str) -> bool:
    try:
        # 1.-Formato JSON valido
        datos = json.loads(json_string)
        
        # 2.-Es un diccionario
        if not isinstance(datos, dict):
            print("ERROR: No es un diccionario")
            return False
        
        # 3. Verificar claves requeridas
        claves_requeridas = ['nombre', 'email', 'edad']
        if not claves_requeridas.issubset(datos.keys()):
            print("ERROR: Faltan claves requeridas (nombre, email, edad)")
            return False
        
        # 4. Verificar edad (número entre 18-100)
        try:
            edad = datos['edad']
            if not (18 <= edad <= 100):
                print(f"ERROR: Edad {edad} fuera de rango (18-100)")
                return False
        except (ValueError, TypeError):
            print("ERROR: Edad debe ser un número")
            return False
        
        # 5. Verificar email contiene @
        if '@' not in datos['email']:
            print("ERROR: Email debe contener '@'")
            return False
        
        print("Usuario válido")
        return True
        
    except json.JSONDecodeError as e:
        print(f"ERROR JSON inválido: {e}")
        return False
    
    except Exception as e:
        print(f"ERROR inesperado: {e}")
        return False
    
def main():
    print(validar_usuario('{"nombre": "Ana", "email": "ana@mail.com", "edad": 25}')) # True
    print(validar_usuario('{"nombre": "Luis", "edad": 30}')) # False (falta email)
    print(validar_usuario('{"nombre": "Eva", "email": "eva.com", "edad": 25}')) # False (email sin @)
    print(validar_usuario('{nombre: "Juan"}')) # False (JSON inválido


if __name__ == "__main__":
    main()