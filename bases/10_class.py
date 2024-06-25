#CLASES#

#para definir utilizamos la palabra reservada class
class MyEmptyPerson: # por buenas practicas del lenguaje se definen con camelcase XxxXxx
    pass # Instruccion del sistema que sirve para intentar ejecutar sin tener nada dentro


print(MyEmptyPerson)


class Person:
    def __init__(self, name, surname) -> None: #el init es reservado del sistema para inicializar un constructor de clase y la flecha es la que devuelve eso se le puede quitar y dejarlo asi 
        #? def __init__(self):
        # pass aqui no hacia nada 
        self.name = name
        self.surname = surname
       

     
my_person = Person("Jhon", "Portilla")
print(f"{my_person.name} {my_person.surname}")

#  #podemos pasar tambien un objeto

class Person2:
    def __init__(self, name, lastname, alias = "Sin Alias"):
        self.full_name = f"{name} {lastname}" #para hacerlo privada colocamos __ antes del full_name y esto nos permite que no se pueda acceder y para acceder tendriamos que hacer una funcion con el get
     # incluyendo funciones dentro de la clase   
    def walk (self):
        print(f"{self.full_name} esta caminando")
        
        
my_other_person = Person2("Juan", "Oliveros")
print(my_other_person.full_name)

# llamamos la funcion de walk
my_other_person.walk()