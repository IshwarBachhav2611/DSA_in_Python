def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def infix_to_postfix(expression):
    stack = []
    output = ""

    for ch in expression:
        if ch.isalnum():
            output += ch

        elif ch == "(":
            stack.append("(")

        elif ch == ")":
            while stack and stack[-1] != "(":
                output += stack.pop()
            stack.pop() #remove '('

        else :
            while stack and precedence(ch) <= precedence(stack[-1]):
                output += stack.pop()
            stack.append(ch)

    while stack:
        output += stack.pop()

    return output

expr = input("Enter Infix Expression :")
print("Postfix Expression : ",infix_to_postfix(expr))
         
                