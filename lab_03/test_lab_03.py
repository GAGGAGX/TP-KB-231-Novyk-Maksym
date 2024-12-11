import unittest
import unittest.mock
import os
import tempfile
import csv

from .student import Student
from .studentList import StudentList
from .CSVManager import CSVManager

class TestStudenList(unittest.TestCase):
    def setUp(self):
        self.test_file = tempfile.NamedTemporaryFile('w', encoding='utf-8',  newline='', delete=False)
        self.test_file_name = self.test_file.name
        self.test_file.close()
        self.data_list = StudentList()
        self.data_list.data_list = []

    def tearDown(self):
        if os.path.exists(self.test_file_name):
            os.remove(self.test_file_name)

    def test_addNewElement(self):
        input_data = ["Test Student", "0631234567", "18", "example@exmp.com"]
    
        with unittest.mock.patch('builtins.input', side_effect=input_data):
            self.data_list.addNewElement()

        self.assertEqual(len(self.data_list.data_list), 1)
        self.assertEqual(self.data_list.data_list[0].name, "Test Student")
        self.assertEqual(self.data_list.data_list[0].phone, "0631234567")
        self.assertEqual(self.data_list.data_list[0].age, "18")
        self.assertEqual(self.data_list.data_list[0].email, "example@exmp.com")

    def test_deleteElement(self):
        input_data = Student(name="Test student", phone="0631234567", age="18", email="example@exmp.com")
        self.data_list.data_list.append(input_data)

        with unittest.mock.patch('builtins.input', side_effect=["Test student"]):
            self.data_list.deleteElement()

        self.assertEqual(len(self.data_list.data_list), 0)

    def test_updateElement(self):
        input_data = Student(name="Test student", phone="0631234567", age="18", email="example@exmp.com")
        self.data_list.data_list.append(input_data)

        input_data = ["Test student", "Updated Student", "0660000000", "20", "example@exmp.com"]

        with unittest.mock.patch('builtins.input', side_effect=input_data):
            self.data_list.updateElement()
        
        self.assertEqual(len(self.data_list.data_list), 1)
        self.assertEqual(self.data_list.data_list[0].name, "Updated Student")
        self.assertEqual(self.data_list.data_list[0].phone, "0660000000")
        self.assertEqual(self.data_list.data_list[0].age, "20")
        self.assertEqual(self.data_list.data_list[0].email, "example@exmp.com")

    def test_importCSV(self):
        fileCSV = CSVManager(self.test_file_name)
        data = [
            {"name": "Emma", "phone": "0664762726", "age": "23", "email": "example@exmp.com"},
            {"name": "Zak", "phone": "0664945504", "age": "22", "email": "example@exmp.com"}
        ]

        with open(self.test_file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["name", "phone", "age", "email"])
            writer.writeheader()
            writer.writerows(data)

        list_from_file = fileCSV.loadCSV()
        
        self.assertEqual(len(list_from_file), 2)
        self.assertEqual(list_from_file[0].name, "Emma")
        self.assertEqual(list_from_file[1].name, "Zak")
        self.assertEqual(list_from_file[0].age, "23")
        self.assertEqual(list_from_file[1].age, "22")
        #os.remove(fileCSV.file_path)

    def test_saveCSV(self):
        fileCSV = CSVManager(self.test_file_name)
        self.data_list.data_list.append(Student(
            name="Jon", 
            phone="0667283939", 
            age="26", 
            email="example@exmp.com"
            ))
        fileCSV.saveCSV(self.data_list.data_list)

        with open(self.test_file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)

            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]['name'], "Jon")
            self.assertEqual(rows[0]['phone'], "0667283939")
            self.assertEqual(rows[0]['age'], "26")
            self.assertEqual(rows[0]['email'], "example@exmp.com")

if __name__ == '__main__':
    unittest.main()
