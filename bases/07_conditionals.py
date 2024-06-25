# CONDITIONALS

#para una condicional tenemos la palabra reservada if

my_condition = False 

if my_condition:
    print("Se ejecuta la condicion cuando el if cuando es verdadero")

print("La ejecucion continua")

my_condition = 5*3

if my_condition % 2 == 0:
    print("el numero es primo")
else:
    print("el numero no es primo")
 
  
my_condition = 5  
    
if my_condition > 10 and my_condition < 20:
    print("mi condicion es mayor que 10 y menor que 20")
elif my_condition < 10:
    print("el numero es menor que 10")
else:
    print("el numero es mayor que 20")


#? para negar una condicion por ejemplo my_string = "" y le pasamos el if not my_string el resultado seria un true porque cumpliria con la condicion


my_string = ""

if not my_string: #como negamos el valor entra aqui
    my_string = "cambiamos la condicion e imprimimos"
    print(my_string)
elif my_string: #aqui entraria si la variable tuviera algo
    print("la string contiene: ", my_string)
