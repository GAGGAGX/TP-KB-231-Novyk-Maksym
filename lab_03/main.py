import sys
from CSVManager import CSVManager
from .studentList import StudentList

def main():
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "log.csv"

    file_manager = CSVManager(file_name)
    students = StudentList()
    students.data_list = file_manager.loadCSV()

    while True:
        choice = input("Specify the action [C create, U update, D delete, P print, S save, X exit and save]: ").upper()
        match choice:
            case "C":
                students.addNewElement()
            case "U":
                students.updateElement()
            case "D":
                students.deleteElement()
            case "P":
                students.printAllList()
            case "S":
                file_manager.saveCSV(students.data_list)
                print("Data saved.")
            case "X":
                file_manager.saveCSV(students.data_list)
                print("Exiting. Data saved.")
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()
