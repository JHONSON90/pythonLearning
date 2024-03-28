"""
    podemos crear cualquier variable con una string
"""

mivariable = "mi primera variable"
my_other_variable = "otra variable"

#podemos concatenarlas
print(mivariable+" "+my_other_variable)

#podemos colocar saltos de linea
print(mivariable+"aqui vamos hacer un salto de linea con el comando \n "+my_other_variable)

#podemos tambien colocar un espacio con el tabulador 
print(mivariable+"aqui vamos hacer un espaciado con tabulador con el comando \t "+my_other_variable)

# ternarios en python
print("---------------------union de variables con strings ---------------------------")

name, surname, age = "Edison", "Portilla", 33

print("Mi nombre es {} {} y mi edad es de {}" .format(name, surname, age))
print(f"Mi nombre es {name} {surname} y mi edad es de {age}")
#Tambien lo podemos hacer de la siguiente manera

print("Mi nombre es %s %s y mi edad es de %d" %(name, surname, age))

# Desempaquetado de caracteres
language = "Python"
a,b,c,d,e,f = language
print(a,b,c,d,e,f)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
