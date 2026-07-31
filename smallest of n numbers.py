n = int(input("Enter how many numbers: "))

smallest = int(input("Enter number: "))

for i in range(1, n):
    num = int(input("Enter number: "))
    if num < smallest:
        smallest = num

print("smallest number =", smallest)
