# Como crear unas tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (35,36,37,38,30,27,17,35)
my_other_tuple = (35,1.77,"Edison", "Portilla")

#acceder a los elementos

print(my_tuple[0])
print(my_other_tuple[-1])
print(my_tuple[0:3])

# operaciones con las tuplas

print(my_tuple.count(35))#cuenta cuantas veces se repite el 35 dentro de la tupla
print(my_other_tuple.count("Edison"))

print(my_tuple.index(38)) #? nos dice en que indice esta el 38 dentro de la tupla

#? las tuplas no se pueden modificar con el acceder a los elementos tampoco nos deja insertar datos
#ejemplo

#my_tuple[0] = 39 nos da error 
#my_tuple[9] = 39 nos da error 

#las tuplas si se pueden unir y crear una nueva 
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)


#? cambiar de tupla a indice y ahora si ya podemos utilizar los metodos de las listas

my_tuple = list(my_tuple) #asi cambiamos a lista
print(type(my_tuple))

my_tuple[7]=47 # cambiamos el valor que esta en el indice 7
my_tuple.insert(1, "Rojo") # insertamos en la posicion 1 el valor de rojo 
my_tuple = tuple(my_tuple) # cambiamos de lista a tupla 
print(type(my_tuple), my_tuple)

#? podemos borrar las tuplas de la siguiente manera

del my_tuple #"del" que es una palabra reservada del sistema para borrar 

print(my_tuple)


