#Como crear listas

my_list = list()
my_other_list = []

#las listas las podemos editar

my_list = [35,36,37,38,30,27,17]
print(my_list)
print(len(my_list))

my_other_list = [35,1.77,"Edison", "Portilla"]
print(type(my_other_list))

#acceder a valores de la lista

print(my_other_list[0]) #accediendo a un valor de la lista
print(my_other_list[0:3]) #accediendo a tres elementos de la lista
print(my_other_list[-1])

# Desempaquetar listas

age, height, name, surname = my_other_list
print(age)
print(height)
print(name)
print(surname)

# tambien podemos desempaquetar colocando el numero de la posicion 
# age,name, height, surname = my_other_list[0],my_other_list[2],my_other_list[1],my_other_list[3]

# Combinar listas

lista_combinada = my_list + my_other_list
print(lista_combinada)

# cambiar de lista a tupla
cambiar_lista = tuple(my_list)
print(type(cambiar_lista))

# Metodos de las listas

print(my_list.count(36)) # sirve para contar elementos dentro de una lista

my_other_list.append("Nicolas")
print(my_other_list)

my_other_list.insert(1,"Rojo")
print(my_other_list)

my_other_list.remove("Rojo")
print(my_other_list)

my_other_list.pop() #al pop si se le pasa el index elimina el elemento que se esta pasando pop(2) e igual se puede guardar el elemento en una variable
print(my_other_list)

del my_other_list[0] #elimina cualquier elemento
print(my_other_list)

my_new_list = my_list.copy()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

my_list.clear()
print(my_list)