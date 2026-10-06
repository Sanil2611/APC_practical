# Problem Statement:
# Create an abstract class Transport with an abstract method calculate_fare(distance).
# Implement subclasses Bus, Train, Taxi, and Flight. Calculate the fare according to
# the transportation type.

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 1.5


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 15


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 5


transports = [Bus(), Train(), Taxi(), Flight()]

for transport in transports:
    print("Fare:", transport.calculate_fare(100))
