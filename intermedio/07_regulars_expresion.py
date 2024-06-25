### EXPRESION REGULARS ###

# es como crear una formula para regular una cadena de texto
# y para utilizarlo se necesita primero importar las expresiones regulares

import re

my_string = "Esta es la clase de Expresiones Regulares: Clase numero 7 grabada en youtube de expresiones"
my_other_string = "Esta no es la clase de Expresiones Regulares"

print(re.match("Esta es la", my_string, re.I))
match = re.match("Esta es la", my_string, re.I)
start, end = match.span()
print(my_string[start:end])

print(re.match("Esta es la", my_other_string))
print(re.match("Expresiones Regulares", my_other_string)) # da none xq solo busca en el principio


match = re.match("Esta es la", my_other_string)
# otra forma de hacerlo es con el 
# if match != None
# if match is not None
if not(match == None):
    print(match)
    start, end = match.span()
    print(my_other_string[start, end])
    
#! search

search = re.search("clase", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

#! findall

findall = re.findall("clase", my_string, re.I ) # el I significa que ignora el formato si mayuscula y minuscula
print(findall)

#! split

split = re.split(":", my_string)
print(split)

#! sub
#sustituye
sub = re.sub("Expresiones", "expresiones", my_string)
sub2 = re.sub("Clase|clase", "CLASE", my_string)
#sub2 = re.sub("[C|c]lase", "CLASE", my_string)
print(sub, sub2)

#! propios patrones Patterns

pattern = r'[Cc]lase'
print(re.findall(pattern, my_string))

pattern = r'[Cc]lase | [Ee]xpresiones'
print(re.findall(pattern, my_string))


pattern = r'[0-9]'
print(re.findall(pattern, my_string))


pattern = r'[a-z]'
print(re.findall(pattern, my_string))