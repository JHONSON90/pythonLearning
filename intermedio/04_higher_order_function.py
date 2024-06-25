### funciones de orden superior ###

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(a, b):
    #normalmente lo hariamos de la siguiente manera:
    ## return a + b + 1 pero como estamos en funciones de orden superior lo hariamos asi
    print(sum_one(a+b))
    
sum_two_values_and_one(5,2)

def sum_two_values_and_add_values(first_value, second_value, f_sum):
    return f_sum(first_value+second_value)

#al momento de llamar la funcion pasamos cual otra funcion hay que concatenar por ejemplo
print(sum_two_values_and_add_values(5,2,sum_one)) #aqui le pasamos por parametro la funcion sum_one y nos adiciona una unidad al momento de sumar los dos primeros numeros

print(sum_two_values_and_add_values(5,2,sum_five))#aqui le pasamos por parametro la funcion sum_five y nos adiciona cinco unidades al momento de sumar los dos primeros numeros

### Clousures ###

def sum_ten():
    def add(value):
        return value + 10
    return add

add_clousure = sum_ten()
print(add_clousure(10))

# pasamos la misma funcion pero le adicionamos parametros a la primera funcion
def sum_ten2(original_value):
    def add2(value):
        return value + 10 + original_value
    return add2

add_clousure2 = sum_ten2(5)
print(add_clousure2(10))
#tambien lo podemos llamar como si lo hicieramos como una lambda 
print(sum_ten2(1)(1))


### FUNCIONES DE ORDEN SUPERIOR QUE YA HAY EN EL LENGUAJE ###

numbers = [ 1,5,6,7,810,901]

#! MAP
# el map recibe dos parametros el primero la funcion y el segundo el iterable

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))

# hacemos lo mismo utilizando una lambda

print(list(map(lambda number: number * 2, numbers )))

#! FILTER

def filter_greater_that_ten(number):
    if number >= 10:
        return True
    return False
    
print(list(filter(filter_greater_that_ten, numbers)))

# podemos hacer lo mismo utilizando lambda

print(list(filter(lambda number: number > 10, numbers)))

#! REDUCE
 #para poder utilizar el reduce necesitamos primero que todo importarlo
 
from  functools import reduce
 
def sum_two_values(number1, number2):
    return number1 + number2

print(reduce(sum_two_values, numbers))