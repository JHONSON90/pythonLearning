### List comprehension ###

my_original_list = [35,24,62,52,30,30,17]

my_list = [i for i in list(range(5))]
print(my_list)

change_my_original_list = [i * 2 for i in my_original_list]
print(change_my_original_list)

multiply_for_my_original_list = [i*i for i in my_original_list]
print(multiply_for_my_original_list)

def mul_five(number):
    return number * 5

my_list = [mul_five(i) for i in range(1, 11)]
print(my_list)