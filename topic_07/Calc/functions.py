import time

class Func:
    def calculate(self, a, b, tool):
        start_act_time = time.perf_counter()
        match tool:
            case "+":
                res = self.sum(a, b)
            case "-":
                res = self.sub(a, b)
            case "*":
                res = self.mult(a, b)
            case "/":
                res = self.div(a, b)
            case "^":
                res = self.deg(a, b)
        elapsed = time.perf_counter() - start_act_time
        return res, elapsed

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            print("Cannot divide by 0")
        else:
            return a / b

    def deg(self, a, b):
        return a ** b
