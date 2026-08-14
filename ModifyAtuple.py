numbers = (10, 20, 30, 40)

my_list = list(numbers)

my_list[1] = 200

numbers = tuple(my_list)

print("Modified tuple:", numbers)
