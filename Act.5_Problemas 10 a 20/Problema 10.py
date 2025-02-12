# Leer un archivo de texto
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print("Contenido del archivo:", contenido)

# Escribir en un archivo
with open("archivo.txt", "w") as archivo:
    archivo.write("Este es un nuevo contenido.")

# Modificar un archivo (agregar texto al final)
with open("archivo.txt", "a") as archivo:
    archivo.write("\nTexto adicional.")
