n = int(input("Enter the number: "))

temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10

if temp == rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
