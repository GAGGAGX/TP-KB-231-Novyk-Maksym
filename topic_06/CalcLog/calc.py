from operations import inp, tool
from functions import sum, sub, mult, div, deg
from datetime import datetime
import time
import os


def calc(a, b):
    act = tool()
    start_act_time = time.perf_counter()
    match act:
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
    end_act_time = time.perf_counter()
    elapsed_time = end_act_time - start_act_time
    print("Result:", res)
    file_path = os.path.join(os.path.dirname(__file__), "log.log")
    act_time = datetime.now().strftime("%A %Y-%m-%d %H:%M:%S")
    with open(file_path, "a") as file:
        file.write(f"{act_time} | {a} {act} {b} = {res} | Elapsed: {elapsed_time:.9f} seconds\n")

while True:
    a, b = inp()
    calc(a, b)
    if (input("Enter exit to end the programm: ")) == "exit":
        exit(0)
        
