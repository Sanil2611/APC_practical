patients = (
    (101, "Rahul", 25, "A+"),
    (102, "Amit", 30, "B+"),
    (103, "Sneha", 22, "O+"),
    (104, "Priya", 28, "A+")
)

print("All Patient Records:")
for patient in patients:
    print(patient)
search_id = int(input("\nEnter Patient ID: "))
found = False
for patient in patients:
    if patient[0] == search_id:
        print("Patient Found:", patient)
        found = True
if not found:
    print("Patient not found")
print("Total Patients =", len(patients))
blood_group = input("\nEnter Blood Group: ")
print("Patients with", blood_group, "blood group:")
for patient in patients:
    if patient[3] == blood_group:
        print(patient)
