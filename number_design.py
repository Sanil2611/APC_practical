n = int(input("Enter n: "))
s = "12345"

for i in range(n):
    for j in range(i + 1):
        print(s[j], end=" ")
    print()
