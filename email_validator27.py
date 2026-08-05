email = input("Enter email: ")

if "@" in email and "." in email and " " not in email:
    print("Valid Email")
else:
    print("Invalid Email")
