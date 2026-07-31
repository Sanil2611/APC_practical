n = int(input("Enter the value: "))

a = 0
b = 1
count = 1

while count <= n:
    print(a, end=" ")
    c = a + b
    a = b
    b = c
    count += 1
