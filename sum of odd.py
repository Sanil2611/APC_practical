n = int(input("Enter a number: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 2

print("Sum of odd numbers up to", n, "is", sum)
