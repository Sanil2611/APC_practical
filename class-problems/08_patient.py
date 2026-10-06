# Problem Statement:
# Create a class Patient containing patient ID, name, age, disease, and consultation fee.
# Define methods to display patient information and calculate the total bill.

class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_information(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee: Rs.", self.consultation_fee)

    def total_bill(self, medicine_bill, test_bill):
        return self.consultation_fee + medicine_bill + test_bill


p = Patient(101, "Amit", 25, "Fever", 500)
p.display_information()

medicine = 800
tests = 300

print("Medicine Bill: Rs.", medicine)
print("Test Bill: Rs.", tests)
print("Total Bill: Rs.", p.total_bill(medicine, tests))
