# Postfix Expression Evaluation

def evaluate_postfix(expression):
    stack = []

    for ch in expression:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a // b)

    return stack[0]


expr = input("Enter Postfix Expression: ")
print("Result:", evaluate_postfix(expr))
