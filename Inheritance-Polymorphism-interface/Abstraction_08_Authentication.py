# Problem Statement:
# Create an abstract class Authentication with an abstract method authenticate().
# Implement the method using Password authentication, OTP authentication, and
# Biometric authentication. Demonstrate abstraction by interacting with objects
# through the abstract interface.

from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using password")


class OTPAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuthentication(Authentication):
    def authenticate(self):
        print("Authenticated using biometric")


methods = [
    PasswordAuthentication(),
    OTPAuthentication(),
    BiometricAuthentication()
]

for method in methods:
    method.authenticate()
