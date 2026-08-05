s = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        count = count + 1
    else:
        result = result + s[i-1] + str(count)
        count = 1

result = result + s[-1] + str(count)

if len(result) < len(s):
    print("Result:", result)
else:
    print("Result:", s)