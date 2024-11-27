def inp():
    while True:
        print("Enter two numbers:")
        a = input("a: ")
        b = input("b: ")
        try:
            a = float(a)
            b = float(b)
            break
        except ValueError:
            print("It's not a number.\n")
    return a, b

def tool():
    while True:
            tool = input("Select a tool: '+' , '-' , '*' , '/' or '^'\n")
            if tool in ['+', '-', '*', '/', '^']:
                return tool
            else:
                print("Invalid operator.\n")