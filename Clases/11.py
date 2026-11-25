# firma(entrada de datos/parametros),cuerpo(proceso:parte logica),salida(return:resultado de la funcion), 
# es posible no tener retorno o uno solo o mas de uno pero ahora trabajamos con el paradigma estructurado, 
# lo tenemos todo legible
# Bajo las reglas del **paradigma estructurado**, mantener esa estructura lineal con una variable de salida (`retorno = ...`) 
# y un único punto de cierre hace que el código sea predecible: sabes exactamente por dónde entra, puedes seguir el hilo de ejecución 
# sin saltos sorpresa y sabes con certeza que terminará en la última línea. 


# break: Rompe únicamente el bucle (for o while) más cercano en el que se encuentra. La función sigue ejecutándose con 
# la línea que esté justo debajo del bucle.

# return: Finaliza inmediatamente toda la función. No importa si está dentro de uno o cinco bucles anidados, mata la función 
# al instante y envía el valor al lugar donde fue llamada.

# si nos pasan una lista vacia que pasa? no itera, el for lo va a intentar [0,0] pero no va a iterar

# Desarrollar una función que reciba 2 listas paralelas y un criterio (asc/desc), si los valores de la lista principal son iguales, 
# deberá ordenar las listas utilizando la segunda lista (Ordenamiento por doble criterio). 
# Devolverá un booleano indicando si pudo ordenar los elementos o no.

def intercambiar_elementos(lista: list, indice_i: int, indice_j: int)->None:
    """
    Recibe una lista y dos inidices, intercambia los valores de ambos indices de la lista.

    Parametro: 
    -lista a intercambiar.
    -indice_i, indice_j, son los inidices de la lista a intercambiar

    Retorno: No tiene retorno (None).
    """
    
    auxiliar = lista[indice_i] 
    lista[indice_i] = lista[indice_j]
    lista[indice_j] = auxiliar



def ordenar_listas(lista_uno: list, lista_dos: list, criterio: str) -> bool:

    """Ordena DOS listas paralelas según el criterio ingresado, en caso de que los elementos de la primer lista sean iguales ordena
    los datos según la lista dos.

    parametros: \n
    -lista_uno (list): Es la lista principal para el criterio de ordenamiento.\n
    -lista_dos (list): Es la lista secundaria paralela a la lista principal.\n
    -criterio (str): 'ascendente' o 'descendente'. Ascendente es para ordenar de menor a mayor. Descendente es para ordenar de mayor a menor.

    Retorno: Return (bool): \n
    -True si pudo ordenar las listas.\n
    -False si no pudo.
    """

    retorno_bandera = False 
    
    if len(lista_uno) == len(lista_dos):

        #burbujeo:
        for i in range(len(lista_uno) - 1): 
            for j in range(i + 1, len(lista_uno)):
                if (criterio == "ascendente" and (lista_uno[i] > lista_uno[j] or (lista_uno[i] == lista_uno[j] and lista_dos[i] > lista_dos[j]))) or (
                    criterio == "descendente" and (lista_uno[i] < lista_uno[j] or (lista_uno[i] == lista_uno[j] and lista_dos[i] < lista_dos[j]))):
                    #swap
                    intercambiar_elementos(lista_uno, i, j)
                    intercambiar_elementos(lista_dos, i, j)
                    retorno_bandera = True 


    return retorno_bandera 



lista_de_nombres = ["pablo", "pedro", "maria", "esteban", "zamurio"]

lista_de_apellidos = ["messi", "quintana", "perez", "vazques", "messi"]

# lista_de_edades = [23, 12, 25, 30, 42]


resultado = ordenar_listas(lista_de_apellidos, lista_de_nombres, "descendente")
print(lista_de_nombres)
print(lista_de_apellidos)

if resultado == True:
    print("Se ordeno.")
else:
    print("no se ordeno.")

