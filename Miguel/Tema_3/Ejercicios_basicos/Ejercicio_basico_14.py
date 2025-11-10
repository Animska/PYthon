from clases import Contacto

class Agenda:
    def __init__(self):
        # Lista de contactos
        self.__contactos = []

    def agregar_contacto(self, contacto):
        # Añade un contacto a la agenda
        self.__contactos.append(contacto)

    def buscar_contacto(self, nombre):
        # Busca el contacto por nombre y lo retorna
        for contacto in self.__contactos:
            if contacto.nombre == nombre:
                return contacto
        return None

    def obtener_telefono(self, nombre):
        # Retorna el teléfono del contacto dado
        contacto = self.buscar_contacto(nombre)
        if contacto:
            return contacto.telefono
        return None

    def obtener_correo(self, nombre):
        # Retorna el correo del contacto dado
        contacto = self.buscar_contacto(nombre)
        if contacto:
            return contacto.correo
        return None

    def cambiar_telefono(self, nombre, nuevo_telefono):
        # Cambia el teléfono del contacto si existe
        contacto = self.buscar_contacto(nombre)
        if contacto:
            contacto.telefono = nuevo_telefono
            return True
        return False

    def cambiar_correo(self, nombre, nuevo_correo):
        # Cambia el correo del contacto si existe
        contacto = self.buscar_contacto(nombre)
        if contacto:
            contacto.correo = nuevo_correo
            return True
        return False

    def listar_contactos(self):
        # Retorna la lista de todos los contactos
        return self.__contactos

    def obtener_numero_contactos(self):
        # Retorna el número total de contactos
        return len(self.__contactos)



c1 = Contacto("Ana López", "123456789", "ana@gmail.com")
c2 = Contacto("Carlos Pérez", "987654321", "carlos@hotmail.com")
c3 = Contacto("Beatriz Gómez", "555444333", "beatriz@yahoo.com")


agenda = Agenda()
agenda.agregar_contacto(c1)
agenda.agregar_contacto(c2)
agenda.agregar_contacto(c3)


print("Buscar 'Carlos Pérez':", agenda.buscar_contacto("Carlos Pérez"))


print("Teléfono de Ana López:", agenda.obtener_telefono("Ana López"))
print("Correo de Beatriz Gómez:", agenda.obtener_correo("Beatriz Gómez"))


print("Cambiar teléfono de Ana López:", agenda.cambiar_telefono("Ana López", "111222333"))
print("Cambiar correo de Carlos Pérez:", agenda.cambiar_correo("Carlos Pérez", "carlos@empresa.com"))


print("\nLista de contactos:")
for contacto in agenda.listar_contactos():
    print(contacto)


print("\nNúmero total de contactos:", agenda.obtener_numero_contactos())
