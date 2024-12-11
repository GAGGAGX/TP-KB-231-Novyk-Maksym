class Student:
    def __init__(self, name, phone, age, email):
        self.name = name
        self.phone = phone
        self.age = age
        self.email = email

    def __str__(self):
        return f"Student name is {self.name}, Phone is {self.phone}, Age is {self.age}, Email is {self.email}"
