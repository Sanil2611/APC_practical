# Python program to find the sum of the series
# 1 + 1/1! + 1/2! + ... + 1/n!

n = int(input("Enter the value of n: "))

sum = 1
fact = 1

for i in range(1, n + 1):
    fact = fact * i
    sum = sum + (1 / fact)

print("Sum of the series =", sum)
