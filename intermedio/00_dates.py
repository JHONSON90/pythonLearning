## Dates ##

import datetime #es una modulo para trabajar con fechas, horas, dias, semanas

now = datetime.datetime.now()
print(now)

day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
print(day, month, year, hour, minute, second)


timestamp = now.timestamp() # es un dato unico que se utiliza como una referencia para despues convertirlo en fecha o algo que podamos utilizar

print(timestamp)

#creando un año nuevo

from datetime import datetime, time, date

year_2025 = datetime(2025,1,1) #para poder usar la funcion datetime primero hay que hacer la importacion sola
print(year_2025)

def print_date(date):
    print(f"Se imprime en el año {date.year}  a los {date.day} del mes de {date.month}")
    
    
print(print_date(year_2025))


#trabajando con el tiempo

current_time = time(9,24,45) #es un objeto que sirva para encapsular tiempo y este le colocamos los parametros para que nos de valores

print(current_time.hour)
print(current_time.minute)
print(current_time.second)


#trabajando con date

current_date = date(2024,12,15)

print(current_date.day)
print(current_date.month)
print(current_date.year)
print(current_date.weekday)

current_date = date.today()

print(current_date.day)
print(current_date.month)
print(current_date.year)
print(current_date.weekday)


#para modificar algun elemento del date 

current_date = date(current_date.year, current_date.month + 1, current_date.day)
print(current_date.month)

#operaciones con fechas

diff = current_date - date.today()
print(current_date)
print(date.today())
print(diff)


from datetime import timedelta
#nos sirve para operar con los datos contenidos en franjas de fechas

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
t3 = t1 - t2
print("t3 =", t3)

init_timedelta = timedelta(200,100,100,weeks=10)
end_timedelta = timedelta(400,100,100,weeks=13)

print(end_timedelta - init_timedelta)
print(end_timedelta + init_timedelta)
print(end_timedelta / init_timedelta)