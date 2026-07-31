s = input("Enter a sentence: ")

words = s.split()

shortest = words[0]

for w in words:
    if len(w) < len(shortest):
        shortest = w

print("shortest word =", shortest)
