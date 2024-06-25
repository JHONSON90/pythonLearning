# FUNCIONES

#sirven para encapsular una solucion a un problema muy concreto, para definir una funcion se inicializa con la palabra def y seguido por el nombre

def my_function():
    print("esto es una funcion")
    

#asi llamamos la funcion y la ejecutamos
my_function()

def generate_full_name ():
    first_name = 'Asabeneh'
    last_name = 'Yetayeh'
    space = ' '
    full_name = first_name + space + last_name
    print(full_name)
generate_full_name () # calling a function

def add_two_numbers ():
    num_one = 2
    num_two = 3
    total = num_one + num_two
    print(total)
add_two_numbers()

def sum_two_values(parametro1,parametro2): #podemos pedir parametros dentro de la misma funcion para que cuando sea llamada se pida el numero de datos necesarios
    print(parametro1 + parametro2)
    
sum_two_values(10,50)
sum_two_values(5051540157, 501984098740)

#? funcion con return

def sum_with_return(a,b):
    return a + b #cuando llamamos el return podemos guardarlo en una nueva variable si no colocamos el return y lo guardamos en una formula nos guardaria un valor None

my_result = sum_with_return(5,10)
print(my_result)

def print_name(name, lastname):
    print(f"{name} {lastname}")
    
print(print_name(lastname="Portilla", name="Jhon Edison"))


def print_name_with_default(name, lastname, alias="Sin Alias"): #podemos colocar un valor por defecto cuando no nos metan la informacion y lo hacemos igualando el valor a lo que nosotros deseemos
     print(f"{name} {lastname} {alias}")
     
print(print_name_with_default("Jhon Edison", "Portilla", "charita"))
print(print_name_with_default("Jhon Edison", "Portilla"))

def print_texts(*text): # cuando colocamos el * le decimos que vamos a recibir el numero de parametros que querramos
    print(text)
    
print(print_texts("Hola", "Claro", "oscuro", "Python"))
print(print_texts("hola"))


def print_texts2(*texts): 
   for text in texts:
    print(text.upper())
    
print(print_texts2("Hola", "Claro", "oscuro", "Python"))
print(print_texts2("hola"))
