from operations import inp, tool
from functions import sum, sub, mult, div, deg

def calc(a, b):
    match tool():
        case "+":
            res = sum(a, b)
        case "-":
            res = sub(a, b)
        case "*":
            res = mult(a, b)
        case "/":
            res = div(a, b)
        case "^":
            res = deg(a, b)
    print("Result:", res)

load = "y"
while load in ['y', 'yes']:
    a, b = inp()
    calc(a, b)
    while True:
        load = input("Again? Y/N: ")
        if load.lower().strip() in ['y', 'n', 'yes', 'no']:
            break
        else:
            print("Selection error.\n")
        
