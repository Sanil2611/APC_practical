n = int(input("Enter a number: "))

sum = 0
i = 0

while i <= n:
    sum += i
    i += 2

print("Sum of even numbers up to", n, "is", sum)
