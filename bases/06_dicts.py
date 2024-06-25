# Diccionarios
"""
los diccionarios nos permite almacenar datos en forma de clave valor    
    """


#? como crear un diccionario

my_dict = dict()
my_other_dict = {}

print(type(my_dict), type(my_other_dict))

my_dict = {
    'first_name':'Jhon',
    'last_name':'Portilla',
    'age':34,
    'country':'Colombia',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(len(my_dict)) # aqui tenemos el valor de 7 que serian las claves que tiene el diccionario

#accediendo al diccionario

print(type(my_dict['skills']))
print(my_dict['first_name']) #si en los corchetes pasamos una clave que no exista nos dara un error para solucionar esto podemos utilizar la funcion get asi como lo miramos a continuacion

print(my_dict.get("age"))
print(my_dict.get("cuidad")) # como no existe la clave nos tira un "None"

#? metodos de los diccionarios

#adicionar datos

my_dict["city"] = "Pasto"
my_dict["skills"].append("GitHUb") #agrega elementos a una lista
print(my_dict)

#modificar datos 

my_dict["city"] = "Ipiales"
print(my_dict)

#borrar datos

my_dict.pop("last_name") #con popitem eliminamos el ultimo item
del my_dict["city"] # elimina la clave y el valor de city
print(my_dict)

#comprobar si existe en un elemento
print("Jhon" in my_dict) # da false xq el dato esta en el valor mas no en la clave osea que el in busca en las claves por eso en el siguiente ejemplo me da true 
print("age" in my_dict) 
print("Jhon" in my_dict['first_name']) #asi me busca en los valores de cada clave

print(my_dict.keys()) # obtengo las claves
print(my_dict.items())
print(my_dict.values())
print(my_dict.fromkeys(("first_name", "age"))) #crea un nuevo diccionario sin valores y esto lo podemos guardar en una variable, esto tambien lo podemos crear pasandole una lista como parametro
#print(my_dict.)

my_new_dict = my_dict.fromkeys(my_dict)#asi utilizamos las llaves de el diccionario de my_dict para colocarle los valores por defecto podemos utilizar el segundo parametro pero ese valor va a todas las claves.
print(my_new_dict)

#cambiar el tipo de dato

print(list(my_dict))
print(tuple(my_dict))
print(set(my_dict))
