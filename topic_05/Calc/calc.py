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

while True:
    a, b = inp()
    calc(a, b)
    if (input("Enter exit to end the programm: ")) == "exit":
        exit(0)
        
