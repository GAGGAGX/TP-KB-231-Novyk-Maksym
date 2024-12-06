from operations import Inp
from functions import Func
from log import Logger

def main():
    inp = Inp()
    calculator = Func()
    logger = Logger()

    while True:
        a, b = inp.num()
        tool = inp.tool()
        res, elapsed_time = calculator.calculate(a, b, tool)
        print("Result:", res)
        logger.log_operation(a, b, tool, res, elapsed_time)

        if input("Enter 'exit' to end the program: ") == "exit":
            exit(0)

main()