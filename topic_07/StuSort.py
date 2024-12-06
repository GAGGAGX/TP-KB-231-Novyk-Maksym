class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age}"
    
students = [
    Student("Alice", 23),
    Student("Bob", 25),
    Student("Charlie", 18),
    Student("Diana", 21)
]

def main():
    for elem in sorted(students, key=lambda s: s.age):
        print(elem)

main()