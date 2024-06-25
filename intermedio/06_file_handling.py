### FILE HANDLING ###

# .txt file
"""
#? para llamar el fichero lo hariamos con Open()

txt_file = open('intermedio/my_file.txt', "w+") # hay modos para poder editar leer y para saber todos los modelos que hay se puede consultar de la siguiente manera python file modes en este caso tenemos el w+ q nos permite  leer y escribir o el r+ nos permite leer y escribir
#print(txt_file.read())
print("------------------- vamos a leer 10 caracteres -------------------")
#print(txt_file.read(10)) #si este viene despues de un read anterior este lo toma como si fuera 10 caracteres posteriores

#print(txt_file.readline())
#print(txt_file.readline())

#print(txt_file.readlines())

#? podemos iterar un archivo de la siguiente manera con un for
for line in txt_file.readlines():
    print(line)


txt_file.write("\n Aunque tambien aprendo y cada dia entiendo mas cosas")
print(txt_file.readlines())
"""

# ahora vamos hacer el ejemplo de crearlo modificarlo, cerrarlo y eliminarlo

import os

txt_file = open('intermedio/my_file.txt', "w+")
txt_file.write("mi nombre es Edison \n me gusta tener todo organizado y planeado, \n estoy aprendiendo python, react y sql no se si sea mucho pero creo que lo necesito jejejeje")


txt_file.write("\n Aunque tambien aprendo y cada dia entiendo mas cosas")

print(txt_file.readlines())
# lo cierro
txt_file.close()

# para eliminar el fichero lo realizariamos de la siguiente manera

#os.remove('intermedio/my_file.txt')


#! archivos json
#es una utilidad que python tiene para poder trabajar con json
import json

json_file = open('intermedio/my_file.json', "w+")

#aqui vamos a definir el json 
json_test = {"Name": "Jhon Edison",
             "SurName": "Portilla",
             "Age": 34,
             "Languages": ["Python","Angular", "React"],
             "WebSite": "Http:jhonportilla.dev"
            }

#vamos a llenar el fichero con los datos que tenemos en el json_test en el archivo json_file y con el 4 espacios al principio
json.dump(json_test, json_file, indent=2)

json_file.close()

with open('intermedio/my_file.json') as my_other_file:
    for line in my_other_file.readlines():
        print(line)

# pasar de un json a un diccionario
json_dict = json.load(open('intermedio/my_file.json'))
print(json_dict)
print(type(json_dict))


# .csv file
import csv 

csv_file = open('intermedio/my_file.csv', "w+")

csv_writer = csv.writer(csv_file)
csv_writer.writerow(["Name", "LastName", "Age", "Language", "Email"])
csv_writer.writerow(["Jhon Edison", "Portilla", 34, "Python", "edisonportillal@gmail.com"])
csv_writer.writerow(["Jhon", "", 4, "React", "Jhon@gmail.com"])
csv_writer.writerow(["Juan", "Tutacha", 39, "", ""])

csv_file.close()
# vamos a imprimir el csv

with open('intermedio/my_file.csv') as my_csv_file:
    for line in my_csv_file.readlines():
        print(line)
        
        
# .xlsx file
#import xlrd # debe instalarse el modulo

# xml file
import xml 