s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagram")
else:
    for ch in s1:
        if s1.count(ch) != s2.count(ch):
            print("Not Anagram")
            break
    else:
        print("Anagram")
