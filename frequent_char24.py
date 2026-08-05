s = input("Enter a string: ")

max_count = 0
max_char = ""

for ch in s:
    if s.count(ch) > max_count:
        max_count = s.count(ch)
        max_char = ch

print("Most frequent character:", max_char)
print("Frequency:", max_count)
