tool = ["(", "+", "-", "*", "/", "^", ")"]

def precedence(act):
    match act:
        case "(":
            return -1
        case "+" | "-":
            return 1
        case "*" | "/":
            return 2
        case "^":
            return 3

def infixToPostfix(expression):
    expElem = expression.split()
    stack = []
    postfix = []
    
    for elem in expElem:
        if elem in tool:
            if elem == tool[0]:
                stack.append(elem)
            elif elem == tool[6]:
                while stack[-1] != tool[0]:
                    postfix.append(stack.pop(-1))
                stack.pop(-1)
            elif len(stack) != 0:
                if precedence(stack[-1]) >= precedence(elem):
                    postfix.append(stack.pop(-1))
                    stack.append(elem)
                else:
                    stack.append(elem)
            else:
                    stack.append(elem)
        else:
            postfix.append(elem)
    postfix.extend(stack[::-1])
    return postfix

def evaluatePostfix(postfixExpression):
    result = []
    for elem in postfixExpression:
        if elem in tool:
            b = float(result[-1])
            a = float(result[-2])
            match elem:
                case '+':
                    result.append(a + b)
                case '-':
                    result.append(a - b)
                case '*':
                    result.append(a * b)
                case '/':
                    result.append(a / b)
                case '^':
                    result.append(a ** b)
            del result[-2]
            del result[-2]
        else:
            result.append(elem)
    return result[0]

def main():
    expression = input("Enter your expression: ")
    seque = infixToPostfix(expression)
    RPN = ""
    for elem in seque:
        RPN += f"{elem} "
    print(f"Polish notation: {RPN}")
    ans = evaluatePostfix(seque)
    print(f"Counting result: {ans}")



if __name__ == "__main__":
    main()
