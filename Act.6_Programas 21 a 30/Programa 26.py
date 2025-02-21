class Agenda:
    def __init__(self):
        self.contactos = {}

    def agregar_contacto(self, nombre, telefono):
        self.contactos[nombre] = telefono

    def obtener_contacto(self, nombre):
        return self.contactos.get(nombre, "Contacto no encontrado")

    def eliminar_contacto(self, nombre):
        if nombre in self.contactos:
            del self.contactos[nombre]
        else:
            return "Contacto no encontrado"

# Ejemplo de uso
agenda = Agenda()
agenda.agregar_contacto("Juan", "123456789")
print(agenda.obtener_contacto("Juan"))
