employee = (101, 102, 103, 104, 105)

id = int(input("Enter employee ID: "))

if id in employee:
    print("Index:", employee.index(id))
else:
    print("ID not found")
