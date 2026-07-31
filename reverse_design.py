n = int(input("Enter n: "))
s = "ABCDE"

for i in range(n, 0, -1):
    for j in range(i):
        print(s[j], end=" ")
    print()
