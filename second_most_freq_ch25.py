s = input("Enter a string: ")

first = 0
second = 0
second_char = ""

for ch in s:
    count = s.count(ch)

    if count > first:
        second = first
        first = count

    elif count < first and count > second:
        second = count
        second_char = ch

print("Second most frequent character:", second_char)
print("Frequency:", second)
