s = input("Enter a string: ")
ch = input("Enter a character: ")

count = 0

for i in s:
    if i == ch:
        count = count + 1

print("Number of times character appears =", count)
