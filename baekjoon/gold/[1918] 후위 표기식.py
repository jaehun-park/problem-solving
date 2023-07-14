expression = list(input())
stack = []

for c in expression:
    if c.isalpha():
        print(c, end="")
    elif c == "(":
        stack.append(c)
    elif c in ["*", "/"]:
        while stack and stack[-1] in ["*", "/"]:
            print(stack.pop(), end="")
        stack.append(c)
    elif c in ["+", "-", ")"]:
        while stack and stack[-1] != "(":
            print(stack.pop(), end="")
        if c in ["+", "-"]:
            stack.append(c)
        elif c == ")":
            stack.pop()

if stack:
    stack.reverse()
    print(*stack, sep="")
