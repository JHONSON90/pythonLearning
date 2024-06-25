# modulos

# nos sirven para importar funciones o componentes

import module

#para hacer uso de la funcion que esta en el otro archivo vamos a llamar el nombre del archivo + "." + la funcion
module.sum(5,10,15)

#importar una sola funcion del fichero de funciones
from functions import print_texts2, generate_full_name

print_texts2("Carrito", "Compras")
generate_full_name()


#tambien podemos traer modulos del sistema
import math #si queremos algo en especifico del modulo lo podemos hacer de la siguiente manera
#? from math import pi #tambien lo podemos renombrar con el as 

print(math.pi)
print(math.pow(2,8))