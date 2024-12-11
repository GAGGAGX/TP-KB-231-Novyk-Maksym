import csv
import os
from .student import Student

class CSVManager:
    def __init__(self, file_path):
        self.file_path = os.path.join(os.path.dirname(__file__), file_path)

    def loadCSV(self):
        data_list = []
        try:
            with open(self.file_path, mode="r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    data_list.append(Student(
                        name = row.get("name", "Unknown"), 
                        phone = row.get("phone", "Unknown"), 
                        age = row.get("age", "Unknown"), 
                        email = row.get("email", "Unknown")
                    ))
            print(f"Data loaded.")
        except FileNotFoundError:
            print("File not found. Starting with an empty list.")
        return data_list

    def saveCSV(self, data_list):
        with open(self.file_path, "w", newline="") as file:
            fieldnames = ["name", "phone", "age", "email"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for student in data_list:
                writer.writerow({"name": student.name, "phone": student.phone, "age": student.age, "email": student.email})
