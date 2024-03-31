# Whiteboard

# Crea un nuevo archivo llamado my_notes.txt.
my_notes = open('my_notes.txt', 'w')

# Método write(): escribir una línea a la vez
my_notes.write("Línea 1: ME LLAMO RAMIRO.\n")
my_notes.write("Línea 2: Estoy aprendiendo de archivos con Python.\n")
my_notes.write("Linea 3: Esta materia es muy divertida pero se viene lo mejor \n")


# Método writelines(): escribir una lista de líneas
lineas = ["Línea 4: Vamos para el otro semestre  .\n", "Línea 5: Finalizando nos vemos en el siguiente nivel \n", "Suerte en la Prueba \n "]
my_notes.writelines(lineas)

my_notes.close()

# Método 1. read()
# Abre el archivo my_notes.txt.
my_notes = open('my_notes.txt', 'r')
#Lee el contenido del archivo línea por línea utilizando el método adecuado.
print('Método 1: read()')
print('--------------------')
print(my_notes.read())
my_notes.close()

# Método 2. readlines()
my_notes = open('my_notes.txt', 'r')
print('Método 2: readlines()')
print('--------------------')
for linea in my_notes.readlines():
    print(linea.rstrip('\n'))
my_notes.close()