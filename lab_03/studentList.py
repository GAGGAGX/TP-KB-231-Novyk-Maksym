from .student import Student

class StudentList:
    def __init__(self):
        self.data_list = []

    def printAllList(self):
        for elem in self.data_list:
            print(elem)

    def addNewElement(self):
        name = input("Enter student name: ")
        phone = input("Enter student phone: ")
        age = input("Enter student age: ")
        email = input("Enter student email: ")
        newItem = Student(name, phone, age, email)
        insertPosition = 0
        for item in self.data_list:
            if name > item.name:
                insertPosition += 1
            else:
                break
        self.data_list.insert(insertPosition, newItem)
        print("New element has been added")

    def deleteElement(self):
        name = input("Please enter name to be deleted: ")
        deletePosition = -1
        for item in self.data_list:
            if name == item.name:
                deletePosition = self.data_list.index(item)
                break
        if deletePosition == -1:
            print("Element was not found")
        else:
            del self.data_list[deletePosition]
            print(f"Element with name {name} has been deleted.")

    def updateElement(self):
        name = input("Please enter name to be updated: ")
        insertPosition = -1
        for item in self.data_list:
            if name == item.name:
                insertPosition = self.data_list.index(item)
                break
        if insertPosition == -1:
            print("Name not found")
        else:
            old_element = self.data_list[insertPosition]
            print(old_element)

            newname = input("Please enter student new name or skip: ") or old_element.name
            newphone = input("Please enter student new phone or skip: ") or old_element.phone
            newage = input("Please enter student new age or skip: ") or old_element.age
            newemail = input("Please enter student new email or skip: ") or old_element.email   

            updateElement = Student(newname, newphone, newage, newemail)
            del self.data_list[insertPosition]
            updatePosition = 0
            for item in self.data_list:
                if newname > item.name:
                    updatePosition += 1
            self.data_list.insert(updatePosition, updateElement)
            print("Element has been updated.")
