numero_uno = 15
numero_dos = 10

#sumar 
print(numero_uno + numero_dos)

#restar
print(numero_uno - numero_dos)

#multiplicar
print(numero_uno * numero_dos)

#dividir        
print(numero_uno / numero_dos)

#potencia
print(numero_uno ** numero_dos)

#modulo
print(numero_uno % numero_dos)  

#operadores logicos

print(numero_uno > numero_dos)
print(numero_uno < numero_dos)
print(numero_uno == numero_dos)
print(numero_uno != numero_dos)

print('Hola '*5)
#cuando con operadores logicos de strings lo hace en comparacion alfabetica

print("hola" >= "Bola")
print("hola" >= "zola")
print(len("hola") >= len("Bola")) #aqui contamos caracteres

#operadores de comparacion 
print("-----------------------------------------------------------")
print(3 > 4 and "hola" > "python")
print(3 < 4 or "hola" > "python")

print(not(3 > 4))


A = ['1','2','3']
for a in A:
    print(2*a)