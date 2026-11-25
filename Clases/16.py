#Archivos

#Dos grandes clases de archivos:
# - De Texto (.TXT, .CSV, etc)
# - Binarios (mp4, img, png, etc)

# 3 pasos
# - APERTURA 
# - MANIPULACION (Lectura y/o escritura)
# - CIERRE

# MODOS DE APERTURA de archivos:

# r -> Lectura
# w -> Escritura
# a -> Anexado


# Funcion open() sirve para abrir archivos. con determinados permisos
# Parametros: ruta del archivo, modo de apertura

# Para crear un archivo podemos abrir en modo escritura
# Escritura (w): si no existe el archivo, lo crea
# si ya existe el archivo, lo abre y borra el contenido, dejandolo vacio

# (a) anexar datos al final del archivo

# Lectura (r): Si el archivo existe lo abre, puede leer el contenido
# Si NO existe arroja un ERROR!


#RUTA RELATIVA -> es la que vamos a usar
# 212-c2/texto.txt

#RUTA ABSOLUTA
# C:/Users/Usuario/Desktop/UTN-2026/212-c2/texto.txt

# Forma basica de apertura y cierre archivos
# try:
#     archivo = open("212-c2/texto.txt", "r")
#     datos = archivo.read() # lee y extrae un string
#     archivo.close()
#     print(datos)
# except:
#     print("El archivo no existe")

# archivo = open("212-c2/texto.txt", "w")
# archivo.write("Chau")
# archivo.close()

# archivo = open("212-c2/texto.txt", "a")
# archivo.write("Pepe") #escribe la cadena 
# archivo.close()

# Forma avanzada de manejo de archivos
# with cierra el archivo automaticamente al terminar su bloque de codigo

ruta = "212-c2/texto.txt"
modo = "r"
# with open(ruta, modo) as archivo:
#     datos = archivo.read()
# # aca esta cerrado el archivo
# print(datos)

# def manejar_archivo(ruta, modo):
#     """ Documentacion"""
#     with open(ruta, modo) as archivo:
#         datos = archivo.readlines() # leer el archivo y devuelve una lista de lineas (str)
#     # aca esta cerrado el archivo
#     print(datos)

# manejar_archivo(ruta, modo)


# lista = ["Juan", "Sofia", "Pepe"]

# with open("212-c2/texto.txt", "w") as archivo:
#     for i in range(len(lista)):
#         if i != len(lista) - 1:
#             archivo.write(lista[i] + ",")
#         else:
#             archivo.write(lista[i] + "\n")

# with open("212-c2/texto.txt", "w") as archivo:
#     archivo.writelines(lista)



#writelines() Recibe un iterable y escribe todos los elementos al archivo 

###### CSV (Comma separated values) ######
# nombre apellido y nota de 3 alumnos

# ESCRIBIR DATOS:
# with open("212/datos.csv", "w") as archivo:
#     archivo.write("Nombre,Apellido,Edad\n")
#     for i in range(3):
#         nombre = input("Ingrese el nombre: ")
#         apellido = input("Ingrese el apellido: ")
#         edad = int(input("Ingrese el edad: "))
#         archivo.write(f"{nombre},{apellido},{edad}\n")


# ANEXADO: 
# with open("212/datos.csv", "a") as archivo:
#     nombre = input("Ingrese el nombre: ")
#     apellido = input("Ingrese el apellido: ")
#     edad = int(input("Ingrese el edad: "))
#     archivo.write(f"{nombre},{apellido},{edad}\n")


# LEER DATOS:

# with open("212/datos.csv", "r") as archivo:
#     datos = archivo.read()

# # datos tiene esto:
# # "Nombre,Apellido,Edad\nJuan,Perez,35\nPepe,Lopez,25\nSofia,Fernandez,28\n"

# Metodos utiles de str / cadenas de caracteres:
# 4 que transforman y manejan minusculas y mayusculas:
# - upper(): pasa todo a mayus.
# - lower(): pasa todo a minus.
# - capitalize(): La primer letra a mayus el resto a minus.
# - title(): La primer letra a mayus el resto a minus (para cada palabra).

# strip(): limpia los extremos de la cadena (inicio y final de la cadena)
# cadena = "   hola mundo!         "
# print(cadena.strip(), end=".")
# cadena = "#######hola # mundo!#####"
# print(cadena.strip("#"), end=".")

# split(): separa cadenas usando el separador pasado por parametro.
# retorna la lista de cadenas separadas.
# cadena = "Pablo Juan Pepe Sofia"
# lista_nombres = cadena.split(" ") # ["Pablo", "Juan", "Pepe", "Sofia"]
# print(lista_nombres)

# join(): une una lista de cadenas entre si, usando un separador.
# cadena_res = "_".join(lista_nombres) # "Pablo_Juan_Pepe_Sofia"
# print(cadena_res)

# saludo = "hOlA mUnDo 5!"
# print(saludo.upper()) # "HOLA MUNDO 5!"
# print(saludo.lower()) # "hola mundo 5!"
# print(saludo.capitalize()) # "Hola mundo 5!"
# print(saludo.title()) # "Hola Mundo 5!"
# print(saludo) # "hOlA mUnDo 5!"



# PARSEO DE DATOS:



with open("212/datos.csv", "r") as archivo:
    datos = archivo.read()

# datos tiene esto:
# "Nombre,Apellido,Edad\nJuan,Perez,35\nPepe,Lopez,25\nSofia,Fernandez,28\n"

# print(datos)
lista_personas = []

datos_limpios = datos.strip()
# print("DESPUES DEL STRIP", datos_limpios)
lista_pers_separadas = datos_limpios.split("\n")
# print("DESPUES DE SPLIT SALTO DE LINEA", lista_pers_separadas)
for i in range(len(lista_pers_separadas)):
    if i == 0: 
        claves = lista_pers_separadas[i].split(",") # ["Nombre", "Apellido", "Edad"]
    else:
        dicc_persona = {}
        valores = lista_pers_separadas[i].split(",") # ["Juan", "Perez", 35]
        for j in range(len(claves)):
            # clave_minus = claves[j].lower()
            dicc_persona.update({claves[j].lower():valores[j]})
        lista_personas.append(dicc_persona)

# print(lista_personas)

# for i in range(len(lista_personas)):
#     print(lista_personas[i])

# print(lista_personas)

# Calcular el promedio de edades de los datos que leemos del archivo:
# suma_edades = 0
# cant_personas = len(lista_personas) # 3
# for i in range(cant_personas): 
#     suma_edades += int(lista_personas[i]["edad"])

# if cant_personas != 0:
#     promedio = suma_edades / cant_personas
#     print("El promedio de edades es: ", promedio)




# BUSQUEDA y Actualizacion:
# for i in range(len(lista_personas)):
#     if lista_personas[i]["nombre"] == "Rodrigo":
#         lista_personas[i]["edad"] = 37
#         # lista_personas[i]["legajo"] = 123 # Si la clave no existe, agrega un item nuevo.
#         # lista_personas[i].update({"edad":37})


# SOBREESCRIBIENDO EL ARCHIVO CON DATOS QUE ESTAN EN MEMORIA DURANTE LA EJECICION
# with open("212/datos.csv", "w") as archivo:
#     archivo.write("Nombre,Apellido,Edad\n")
#     for i in range(len(lista_personas)):
#         archivo.write(f"{lista_personas[i]["nombre"]},{lista_personas[i]["apellido"]},{lista_personas[i]["edad"]}\n")


def mostrar_diccionarios(lista:list[dict])->None:
    """Documentacion"""
    for i in range(len(lista)):
        if i == 0:
            for clave in lista[i].keys():
                print(f"{clave:<20}", end="")
            print("\n" + "-" * (20 * len(lista[i].keys())))
        for clave in lista[i].keys():
            #print(f"{(lista[i][clave]):^20}", end="") # Centrado
            #print(f"{(lista[i][clave]):>20}", end="") # Alineado a la der
            print(f"{(lista[i][clave]):<20}", end="") # Alineado a la izq (defecto)
        print()



mostrar_diccionarios(lista_personas)


# Archivos JSON (JavaScript Object Notation)

import json

# Escritura: 
# with open("212/alumnos.json", "w") as archivo:
#     json.dump(lista_personas, archivo, indent=4)

# Lectura
with open("212/alumnos.json", "r") as archivo:
    datos = json.load(archivo)

print(datos)