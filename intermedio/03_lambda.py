### Lambda ###

#  son funciones anonimas y se pueden almacenar en una variable

lambda first_value, second_value: first_value + second_value

sum_two_values = lambda first_value, second_value: print(first_value + second_value)
sum_two_values(2 , 4)

# podemos usar lambda dentro de una funcion

def sum_three_values(value):
    return lambda first_value, second_value: print(first_value + second_value + value)

sum_three_values(5)(2,4)