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

# Metodos de las listas

print(my_list.count(36))



# cambiar de lista a tupla
cambiar_lista = tuple(my_list)
print(type(cambiar_lista))

