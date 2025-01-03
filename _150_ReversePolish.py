def evalRPN(tokens) -> int:
    stack = []

    for token in tokens:
        try:
            stack.append(int(token))
        except:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    a = stack.pop()
                    b = stack.pop()
                    quotient = int(b / a)
                    stack.append(quotient)
        
    return stack[0]
    

print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
))