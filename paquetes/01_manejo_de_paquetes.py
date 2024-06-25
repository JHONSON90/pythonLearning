### MANEJO DE PAQUETES ####

#! QUE ES PIP 
# se llama python package index 

print("hola mundo")

import numpy as np 

numpy_array = np.array([1,2,3, 45,49,62,95])

print(type(numpy_array))

print(numpy_array * 2)

#? pip list nos permite sacar un listado de los paquetes instalados
#! pip uninstall pandas - permite eliminar un paquete
# pip show paquete - permite dar informacion sobre el paquetes


import requests as rq

response = rq.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())

