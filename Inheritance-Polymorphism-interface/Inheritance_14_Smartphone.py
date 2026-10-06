# Problem Statement:
# Create classes Camera and Phone. The Camera class should provide methods for taking
# photographs, while Phone should provide methods for making calls. Create a Smartphone
# class inheriting from both.

class Camera:
    def take_photo(self):
        print("Photograph taken")


class Phone:
    def make_call(self, number):
        print("Calling", number)


class Smartphone(Camera, Phone):
    pass


s = Smartphone()
s.take_photo()
s.make_call("9876543210")
