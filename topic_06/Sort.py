students = [
    {'name': "Richard", 'mark': 84},
    {'name': "Gogi", 'mark': 65},
    {'name': "James", 'mark': 98},
    {'name': "Bob", 'mark': 23},
    {'name': "Biden", 'mark': 87},
    {'name': "Jon", 'mark': 90}
]

def sort(key):
    for elem in sorted(students, key=lambda x: x[key]):
        print(f"Name — {elem['name']} | Mark — {elem['mark']}")

while True:
    act = input("Select sorting: N — name, M — mark, or 'exit': ").lower()
    match act:
        case "exit":
            break
        case "n":
            sort('name')
        case "m":
            sort('mark')
        case _:
            print("Selection error.\n")
