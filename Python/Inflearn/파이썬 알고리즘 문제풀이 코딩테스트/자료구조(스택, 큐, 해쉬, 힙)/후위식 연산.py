a = input()
stack = []

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x == '+':
            tmp = stack.pop() + stack.pop()
            stack.append(tmp)

        elif x == '-':
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            stack.append(tmp2 - tmp1)

        elif x == '*':
            tmp = stack.pop() * stack.pop()
            stack.append(tmp)

        elif x == '/':
            tmp1 = stack.pop()
            tmp2 = stack.pop()
            stack.append(tmp2 / tmp1)

print(int(stack[0]))