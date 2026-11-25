# Metodos de LISTAS.
# from random import *
import random



# ESTA INTRO, NO ENTRA AL PARCIAL.
# POO:


# Abstracto: un plano / molde (clase)
# Concreto: un objeto / instancia de la clase (objeto)

# CARACTERISTICAS (atributos) y COMPORTAMIENTOS (metodos).


# numero = 5
# print(type(numero))

class Persona():
    # Metodo CONSTRUCTOR:
    def __init__(self, nombre:str, aplldo:str, edad:int):
        # self.atributo = parametro
        self.nombre = nombre 
        self.apellido = aplldo
        self.edad = edad
        self.regular = True

    # Comportamiento saludo
    # METODO (una funcion que le pertenece a una clase especifica) SALUDAR 
    def saludar(self)->str:
        """Saludar de Persona"""
        #print(f"Hola mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años.")
        return f"Hola mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años."

    def descansar(self, material:str):
        print(f"La persona {self.nombre} esta descansando sobre el {material}. ZZZZ")

    
class Perro():
    def __init__(self, nombre:str, color:str):
        self.nombre = nombre
        self.color = color
    def saludar(self)->str:
        """Saludar de Perro"""
        return "Guau!!!"


# SON FUNCIONES
# len()
# print()
# input()

def saludar():
    print("HOLA MUNDO")

persona_a = Persona("Pepe", "Lopez", random.randint(30, 35)) # modulo random, funcion randint
persona_b = Persona("Juan", "Perez", 40)
persona_c = Persona("Sofia", "Gomez", 50)
persona_d = Persona("Nicolas", "Gimenez", 43)

perrito = Perro("Firulais", "Gris")


persona_c.saludar() # ES UN METODO (tiene punto y no es un MODULO)
persona_c.descansar("Colchon") # TAMBIEN ES UN METODO (tiene punto y no es un MODULO)
saludar() # ES UNA FUNCION!

# print(persona_a.saludar())
# print(persona_b.saludar())
# perrito.saludar() # Guau!!!

# persona_a.saludar()

# persona_b.descansar()

lista_personas = [persona_a, persona_b, persona_c, persona_d, perrito]
for i in range(len(lista_personas)):
    print(lista_personas[i].saludar())
# print(type(persona_a))
# print(lista_personas)
# print(persona_a.nombre) # Pepe
# print(persona_a.apellido) # Lopez
# print(persona_a.edad) # entre 30 y 40
# print(persona_a.regular) # True

# print("*" * 30)
# print(persona_b.nombre) # Juan
# print(persona_b.apellido) # Perez
# print(persona_b.edad) # 40
# persona_b.regular = False # le cambio el estado a irregular de la persona_b
# print(persona_b.regular) # False
# print("*" * 30)

# print(persona_a) # Muestra el ID del objeto.
# print(persona_b) # Muestra el ID del objeto.

# Otros constructores / Casteos
# int()
# float()
# str()
# list()
# range(2, 5) # [2, 3, 4]


