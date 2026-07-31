# Python program to print the series 1 2 4 8 16 32 ... (n terms)

n = int(input("Enter the number of terms: "))
term = 1

for i in range(n):
    print(term)
    term = term * 2
