# loops o bucles

#? while es una palabra reservada y nos sirve para iterar. El while funciona que mientras sea verdadero se ejecute el codigo

my_condition = 0

while my_condition < 20:
    my_condition += 2 #el += me esta incrementando de uno en uno mi condicion es para no coloocar my_condition = my_condition + 1
    if my_condition == 10:
        print("mi condicion ha llegado a 10")
        continue # permite que la ejecucion lo salte y continue en el siguiente 
    
    #podemos colocar un break que nos sirve para parar la ejecucion y lo hariamos de la siguiente manera 
    if my_condition == 15:
        print("la condicion ya llego a 18")
        break #cuando la condicion llegue a 18 imprime lo que esta en el print y se detiene la ejecucion
    print(my_condition)

print("La ejecucion continua")

#? bucle for nos sirve para iterar un listado de elementos y esto se repetira las veces que sea necesario hasta cubrir con toda la lista

my_list = [35,24,38,49,50,52,20]

my_tuple = (35,36,37,38,30,27,17,35)

my_set = {1,2,4,6,8,10,12,14,16}

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

# for es la palabra reservada, elemento es un nombre que se le da a cada elemento que esta dentro de la lista se la puede llamar de cualquier manera y my_list es el nombre de la lista. aunque no solo sirve con listas si no con cualquier dato puede ser una tupla un set o un dict
for element in my_list: 
    print("este es un elemento de una lista" ,element)

for element in my_tuple:
    print("Este elemento es de una tupla: ", element )

for element in my_set:
    print("Este elemento es de un set: ", element )

for element in my_dict: #aqui imprime todos las claves
    print("Este elemento es de un diccionario: ", element )
    
for element, value in my_dict.items(): #aqui imprime todos las claves y sus valores
    print("Este elemento es de un diccionario: ", element, value )

for values in my_dict.values(): #aqui imprime todos los valores
    print("Este elemento es de un diccionario: ", values )
    
#en los bucles for tambien tenemos el break y el continue

for element in my_dict: 
    print("Este elemento es de un diccionario: ", element )
    if element == "age":
        break  #la ejecucion se para cuando encuentra el age y lo que sigue no esta en la impresion


for element in my_dict: 
    print("Este elemento es de un diccionario: ", element )
    if element == "age":
        continue #nos para el codigo y sigue con el siguiente elemento
    print("se ejecuta")
    
    
# syntax de la iteracion dentro de un rango
#? for iterator in range(start, end, step):