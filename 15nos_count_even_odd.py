numbers = (10, 15, 22, 7, 18, 25, 30, 11, 14, 9, 16, 21, 8, 13, 20)

even = 0
odd = 0

for num in numbers:
    if num % 2 == 0:
        even = even + 1
    else:
        odd = odd + 1

print("Even numbers =", even)
print("Odd numbers =", odd)
