# excepciones o manejo de errores

numero1 = "5"
numero2 = 15
numero3 = 20

#con el try except podemos manejar los errores en este caso nos maneja el error con el except
try:
    print(numero1+numero2)
    print("no se ha producido un error")
except:
    print("Se ha producido un error en la suma")
finally: # imprime asi la ejecucion tenga errores - y se ejecuta siempre
    print("La ejecucion conginua") 

# en este caso nos suma xq nos entra en el try
  
try:
    print(numero3+numero2)
    print("no se ha producido un error")
except:
    print("Se ha producido un error en la suma")
else:
    print("continua la ejecucion")  #esta linea solo se ejecuta siempre y cuando no haya errores
finally:
    print("La ejecucion conginua")
    
#excepciones por tipo de error

try:
    print(numero1+numero2)
    print("no se ha producido un error")
except TypeError:
    print("Se ha producido un error en la suma debido a un dato no valido")
except ValueError:
    print("Se ha producido un error en la suma debido a un valor de tu codigo")

# Captura de la informacion de la excepcion o error

try:
    print(numero1 + numero2)
    print("no se ha producido un error")
except Exception as error : #para capturar todo tipo de errores y no por tipo como el ejemplo anterior (TypeError, ValueError etc)
    print(error) #montamos que tipo de error es y mas informacion sobre el error 
