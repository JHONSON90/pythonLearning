# sets 
"""
la diferencia entre listas o tuplas y sets es que no es una estructura ordenada, no permite valores duplicados     
"""
#asi creamos los sets
my_set = set()
my_other_set = {} # se inicializan como diccionario pero al colocarle los datos pasa a ser un set 

my_set = {1,2,4,6,8,10,12,14,16}
my_other_set = {"Edison", "Portilla", 34}

print(type(my_other_set), my_other_set)

#sacar el largo
print(len(my_other_set))

#? metodos de los sets

my_other_set.add("cualquiercosa")
print(my_other_set)

# vamos a meter el mismo dato en el set y no va a dejar hacerlo asi como lo miramos en el siguiente ejemplo
my_other_set.add("cualquiercosa")
print(my_other_set)

print("Edison" in my_other_set) #vamos a comprobar si existe Edison en mi set
print("Jhon" in my_other_set) #comprobamos si existe Jhon en mi set

my_other_set.remove("cualquiercosa") #vamos a eliminar el cualquiercosa con el metodo remove
print(my_other_set)

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_other_set)) #saca la los diferentes que tiene el new set quitando my other set

my_other_set.clear() # borramos los datos del set
print(my_other_set)

del my_other_set # borramos el set

#cambiar de set a lista

my_list = list(my_set)
print(type(my_list))




#print(my_other_set[0])