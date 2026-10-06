# Problem Statement:
# Create an abstract class Patient with abstract methods calculate_bill() and treatment().
# Derive InPatient, OutPatient, and EmergencyPatient classes and implement the methods
# according to the patient type.

from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        return "In-patient treatment"


class OutPatient(Patient):
    def calculate_bill(self):
        return 1000

    def treatment(self):
        return "Out-patient treatment"


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 8000

    def treatment(self):
        return "Emergency treatment"


patients = [InPatient(), OutPatient(), EmergencyPatient()]

for patient in patients:
    print(patient.treatment())
    print("Bill:", patient.calculate_bill())
