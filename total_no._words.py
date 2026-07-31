s = input("Enter a sentence: ")

count = 1

for ch in s:
    if ch == " ":
        count = count + 1

print("Total words =", count)
