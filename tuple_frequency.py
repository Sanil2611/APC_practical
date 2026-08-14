numbers = (10, 20, 10, 30, 20, 10, 40, 30)

checked = ()

for num in numbers:
    if num not in checked:
        print(num, "=", numbers.count(num))
        checked = checked + (num,)
