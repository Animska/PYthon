# Comprueba si un usuario tiene los permisos mínimos requeridos.
usuario = {"read", "write"}
requeridos = {"read"}

print("permisos permitidos") if requeridos in usuario else print("permisos denegados")