marital = input("Enter marital status (married/unmarried): ")
gender = input("Enter gender (male/female): ")
age = int(input("Enter age: "))

if marital == "married":
    print("Driver is Insured")
elif marital == "unmarried" and gender == "male" and age > 30:
    print("Driver is Insured")
elif marital == "unmarried" and gender == "female" and age > 25:
    print("Driver is Insured")
else:
    print("Driver is Not Insured")
