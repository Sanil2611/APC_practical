# Problem Statement:
# Create an abstract class CloudStorage with abstract methods upload_file(),
# download_file(), and delete_file(). Create subclasses representing different
# storage services and implement the operations.

from abc import ABC, abstractmethod

class CloudStorage(ABC):
    @abstractmethod
    def upload_file(self, file):
        pass

    @abstractmethod
    def download_file(self, file):
        pass

    @abstractmethod
    def delete_file(self, file):
        pass


class GoogleDrive(CloudStorage):
    def upload_file(self, file):
        print("Uploading", file, "to Google Drive")

    def download_file(self, file):
        print("Downloading", file, "from Google Drive")

    def delete_file(self, file):
        print("Deleting", file, "from Google Drive")


class OneDrive(CloudStorage):
    def upload_file(self, file):
        print("Uploading", file, "to OneDrive")

    def download_file(self, file):
        print("Downloading", file, "from OneDrive")

    def delete_file(self, file):
        print("Deleting", file, "from OneDrive")


services = [GoogleDrive(), OneDrive()]

for service in services:
    service.upload_file("data.txt")
    service.download_file("data.txt")
    service.delete_file("data.txt")
