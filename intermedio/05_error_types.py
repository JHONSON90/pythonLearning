### Error Types ###

# SyntaxError

# print "Hola Mundo!!!!" #! este es el error y nos quiere decir que esta mal escrito
print ("Hola Mundo!!!!")

# NameError

#print(language) #! el error es xq la variable no esta definida o no esta escrita antes de esta linea

language = "Python"
print(language)

# IndexError

my_list = ["python", "javascript", "react"]
#print(my_list[10]) #! el error es que esta pidiendo imprimir un elemento que no existe en el listado solo existen tres elementos en la lista y queremos acceder al elemento 10
print(my_list[2])

# ModuleNotFoundError

# import maths #! el error se da por que estamos importando un modulo que no existe y esta mal escrito

import math

# AtributeError

# print(math.PI) #! el error se da xq la propiedad esta puesta en mayuscula y se tendria que escribir en minuscula
print(math.pi)

# KeyError

users = {'name':'Asab', 'age':250, 'country':'Finland'}
print(users['name'])
# print(users['county']) #! el error se da por que el nombre de la propuedad esta mal escrito

# TypeError
# print(my_list["nombre"]) #! el error se da por que estamos accediendo a una lista y para hacerlo lo tendriamos que hacerlo con un numero entero las listas no tienen clave valor, tambien se da por error de tipificacion "sumar un string"
print(my_list[0])

# ImportError

#from math import PI #! El error se de es xq el PI esta en mayuscula ademas al tirar el codigo le da documentacion de la libreria

from math import pi


#ValueError
my_int = "10-A"
print(int(my_int))