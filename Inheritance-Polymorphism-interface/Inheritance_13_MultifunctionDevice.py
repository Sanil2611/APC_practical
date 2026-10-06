# Problem Statement:
# Create classes Printer and Scanner with suitable methods for printing and scanning documents.
# Create a MultifunctionDevice class that inherits from both and supports both operations.

class Printer:
    def print_document(self):
        print("Printing document")


class Scanner:
    def scan_document(self):
        print("Scanning document")


class MultifunctionDevice(Printer, Scanner):
    pass


device = MultifunctionDevice()
device.print_document()
device.scan_document()
