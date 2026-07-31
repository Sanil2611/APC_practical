n = int(input("Enter n: "))
s = "ABCDE"

for i in range(n):
    for j in range(i + 1):
        print(s[j], end=" ")
    print()
