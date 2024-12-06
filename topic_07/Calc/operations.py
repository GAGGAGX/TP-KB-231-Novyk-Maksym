class Inp:
    def num(self):
        while True:
            try:
                a = float(input("a: "))
                b = float(input("b: "))
                return a, b
            except ValueError:
                print("It's not a number.\n")

    def tool(self):
        while True:
            tool = input("Select a tool: '+' , '-' , '*' , '/' or '^'\n")
            if tool in ['+', '-', '*', '/', '^']:
                return tool
            else:
                print("Invalid tool.\n")
