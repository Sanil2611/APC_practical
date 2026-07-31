s = input("Enter a string: ")

upper = 0
lower = 0

for ch in s:
    if ch >= 'A' and ch <= 'Z':
        upper = upper + 1
    elif ch >= 'a' and ch <= 'z':
        lower = lower + 1

print("Uppercase =", upper)
print("Lowercase =", lower)
