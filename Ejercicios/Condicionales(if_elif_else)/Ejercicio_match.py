# Abril Dobal
# Match
# Una agencia de viajes nos pide informar si hacemos viajes a lugares según la estación del año. 
# En caso de hacerlo mostrar por print  el mensaje “Se viaja”, caso contrario mostrar “No se viaja”. 
# Si es invierno: solo se viaja a Bariloche.
# Si es verano: se viaja a Mar del plata y Cataratas.
# Si es otoño: se viaja a todos los lugares.
# Si es primavera: se viaja a todos los lugares menos Bariloche.


estacion = input("Ingrese la estación del año (Invierno / Verano / Otoño / Primavera): ")
lugar = input("Ingrese el lugar (Bariloche / Mar del Plata / Cataratas): ")

match estacion:
    case "Invierno":
        if lugar == "Bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case "Verano":
        if lugar == "Mar del Plata" or lugar == "Cataratas":
            print("Se viaja")
        else:
            print("No se viaja")
    case "Otoño":
        print("Se viaja")  # A todos los lugares.
    case "Primavera":
        if lugar == "Bariloche":
            print("No se viaja")
        else:
            print("Se viaja")
    case _:  # Caso por defecto (default), debe ir como último caso.
        print("Error, estación inválida.")