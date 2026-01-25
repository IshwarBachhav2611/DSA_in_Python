# Infix to Prefix Conversion

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_prefix(expression):
    expression = expression[::-1]
    expression = expression.replace('(', 'temp')
    expression = expression.replace(')', '(')
    expression = expression.replace('temp', ')')

    stack = []
    output = ""

    for ch in expression:
        if ch.isalnum():
            output += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                output += stack.pop()
            stack.pop()

        else:
            while stack and precedence(ch) < precedence(stack[-1]):
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output[::-1]


expr = input("Enter Infix Expression: ")
print("Prefix Expression:", infix_to_prefix(expr))
