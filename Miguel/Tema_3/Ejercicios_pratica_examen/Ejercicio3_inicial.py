CONTRASENAS_PROHIBIDAS = ["12345678", "password", "qwertyui", "letmein1", "welcome"]

def procesar_password(password: str) -> str:
    if 'a' not in password:
        return "Error: La contaseña debe contener el caracter 'a'"
    
    id_a = password.index('a')
    subpassword = password[id_a+1:id_a+9]
    if len(subpassword) < 8:
        return "Error: La contraseña debe contener al menos una letra 'a' seguida de más caracteres."
    
    if subpassword in CONTRASENAS_PROHIBIDAS:
        return "Error: La contraseña generada está en la lista de contraseñas prohibidas."
    
    return subpassword

# Prueba
password_test = "banana12345678"
password_test_mal = "bapasswordnana12345678"
resultado = procesar_password(password_test)
print("\n--- EJERCICIO: PROCESAMIENTO DE CONTRASEÑA ---")
print(f"Contraseña original: {password_test}")
print(f"Resultado del procesamiento: {resultado}")