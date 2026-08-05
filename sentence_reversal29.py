s = input("Enter a sentence: ")

words = s.split()

words = words[::-1]

result = " ".join(words)

print("Reversed sentence:", result)
