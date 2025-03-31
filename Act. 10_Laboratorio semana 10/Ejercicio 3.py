contactos = []

def agregar_contacto(nombre, numero, correo):
    contactos.append((nombre, numero, correo))

def buscar_contacto(nombre):
    for contacto in contactos:
        if contacto[0] == nombre:
            return contacto
    return None

def listar_contactos():
    for contacto in sorted(contactos, key=lambda x: x[0]):
        print(f"Nombre: {contacto[0]}, Número: {contacto[1]}, Correo: {contacto[2]}")

# Ejemplo de uso:
agregar_contacto("Juan", "123456789", "juan@mail.com")
agregar_contacto("Ana", "987654321", "ana@mail.com")
listar_contactos()
