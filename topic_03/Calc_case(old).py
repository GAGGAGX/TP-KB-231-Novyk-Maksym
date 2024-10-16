def inp():
    print("Enter two numbers:")
    a = int(input("a: "))
    b = int(input("b: "))
    return a,b

def calc(a, b):
    tool = input("Select a tool: '+' , '-' , '*' , '/' or '^'\n")
    if b == 0 and tool == "/":
        print("Cannot divide by 0")
    else:
        match tool:
            case "+":
                return a + b
            case "-":
                return a - b
            case "*":
                return a * b
            case "/":
                return a / b
            case "^":
                return a ** b
            case _:
                print("Input error.")
   
exreload = 1
while exreload != 0:
    a, b = inp()
    result = calc(a, b)
    print("Result:", result)
    exreload = int(input("Again? 1/0: ")) 
