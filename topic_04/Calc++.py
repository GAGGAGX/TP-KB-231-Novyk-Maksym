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

def calc(a, b):
    while True:
        tool = input("Select a tool: '+' , '-' , '*' , '/' or '^'\n")
        if tool in ['+', '-', '*', '/', '^']:
            break
        else:
            print("Invalid operator.\n")
    match tool:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b == 0:
                print("Cannot divide by 0")
            else:
                return a / b
        case "^":
            return a ** b
        
exreload = "y"
while exreload in ['y', 'yes']:
    a, b = inp()
    result = calc(a, b)
    print("Result:", result)
    while True:
        exreload = input("Again? Y/N: ")
        if exreload.lower().strip() in ['y', 'n', 'yes', 'no']:
            break
        else:
            print("Selection error.\n")
