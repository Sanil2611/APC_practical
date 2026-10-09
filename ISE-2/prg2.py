f = open("test.txt", "w")

n = int(input("Enter number of students: "))

for i in range(n):
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    marks = input("Enter marks: ")
    f.write(roll + " " + name + " " + marks + "\n")

f.close()


f = open("test.txt", "r")
r = input("Enter roll number to search: ")

for line in f:
    data = line.split()
    if data[0] == r:
        print("Name:", data[1])
        print("Marks:", data[2])
        break
else:
    print("Record not found")

f.close()
