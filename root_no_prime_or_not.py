# Check whether square root of a number is prime or not

n = int(input("Enter a number: "))
root = 0
for i in range(1, n + 1):
    if i * i == n:
        root = i
        break
prime = True
if root < 2:
    prime = False
else:
    for i in range(2, root):
        if root % i == 0:
            prime = False
            break
if prime:
    print("Square root is Prime")
else:
    print("Square root is Not Prime")
