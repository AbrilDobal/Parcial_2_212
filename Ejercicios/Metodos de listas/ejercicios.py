# Declarar una lista vacía, y manipularla mediante métodos de listas, mostrando los resultados
# después de cada operación:

alumnos = []
print("Lista inicial vacía:", alumnos)
print("-" * 50)

# 1) Agregar 3 nombres de alumnos (ingresados por el usuario) al final de la lista.
print("--- 1) Agregar 3 nombres al final ---")
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    alumnos.append(nombre)
print("Lista actual:", alumnos)
print("-" * 50)

# 2) Insertar un 4to nombre de alumno (ingresado por el usuario) al principio de la lista.
print("--- 2) Insertar un nombre al principio ---")
nombre_principio = input("Ingrese un nombre para insertar al principio: ")
alumnos.insert(0, nombre_principio)
print("Lista actual:", alumnos)
print("-" * 50)

# 3) Extender la lista agregando 2 nombres adicionales al principio de la misma.
print("--- 3) Extender agregando 2 nombres al principio ---")
# Como .extend() agrega elementos al final, creamos una lista auxiliar con los 
# nuevos nombres y extendemos esa lista auxiliar con la original.
nombres_extra = []
for i in range(2):
    nombres_extra.append(input(f"Ingrese nombre extra {i+1} para el principio: "))

nombres_extra.extend(alumnos)
alumnos = nombres_extra
print("Lista actual:", alumnos)
print("-" * 50)

# 4) Contar e informar cuántas veces aparece un nombre ingresado por el usuario.
print("--- 4) Contar apariciones de un nombre ---")
nombre_buscar = input("Ingrese un nombre para contar cuántas veces aparece: ")
cantidad = alumnos.count(nombre_buscar)
print(f"El nombre '{nombre_buscar}' aparece {cantidad} vez/veces en la lista.")
print("Lista actual:", alumnos)
print("-" * 50)

# 5) Eliminar de la lista un nombre ingresado por el usuario.
print("--- 5) Eliminar un nombre específico ---")
nombre_eliminar = input("Ingrese el nombre que desea eliminar: ")
try:
    alumnos.remove(nombre_eliminar)
    print(f"Se eliminó correctamente a '{nombre_eliminar}'.")
except ValueError:
    print(f"El nombre '{nombre_eliminar}' no se encuentra en la lista.")
print("Lista actual:", alumnos)
print("-" * 50)

# 6) Eliminar el penúltimo nombre de la lista e informar qué nombre se eliminó.
print("--- 6) Eliminar el penúltimo nombre ---")
if len(alumnos) >= 2:
    # El penúltimo índice corresponde a la posición -2
    nombre_eliminado = alumnos.pop(-2)
    print(f"Se eliminó el penúltimo nombre: '{nombre_eliminado}'.")
else:
    print("No hay suficientes elementos para eliminar el penúltimo.")
print("Lista actual:", alumnos)
print("-" * 50)

# 7) Ingresar un nombre por consola, buscarlo e informar su índice.
print("--- 7) Buscar el índice de un nombre ---")
nombre_indice = input("Ingrese un nombre para buscar su índice: ")
try:
    indice = alumnos.index(nombre_indice)
    print(f"El nombre '{nombre_indice}' se encuentra en el índice {indice}.")
except ValueError:
    print(f"El nombre '{nombre_indice}' no existe en la lista.")
print("Lista actual:", alumnos)
print("-" * 50)

# 8) Ordenar los nombres descendentemente.
print("--- 8) Ordenar descendentemente ---")
alumnos.sort(reverse=True)
print("Lista ordenada descendentemente:", alumnos)
print("-" * 50)

# 9) Crear una copia de la lista.
print("--- 9) Crear una copia de la lista ---")
alumnos_copia = alumnos.copy()
print("Copia creada exitosamente.")
print("Lista original:", alumnos)
print("Lista copia   :", alumnos_copia)
print("-" * 50)

# 10) Limpiar la lista original eliminando todos sus elementos, mostrar la lista original y la copia.
print("--- 10) Limpiar la lista original ---")
alumnos.clear()
print("Lista original después de .clear():", alumnos)
print("Lista copia (intacta)            :", alumnos_copia)
print("=" * 50)