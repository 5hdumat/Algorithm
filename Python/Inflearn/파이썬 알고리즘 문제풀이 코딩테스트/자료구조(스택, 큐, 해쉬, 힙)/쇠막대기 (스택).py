'''
stack: LIFO
'''
s = input()
stack = []
sum = 0

for i in range(len(s)):
    if s[i] == '(':
        stack.append((s[i]))
    else:
        stack.pop()

        if s[i-1] == '(': # '('가 아닌 else문 이니 and s[i] == ')' 생략
            # stack.pop()
            sum += len(stack)
        elif s[i-1] == ')':
            # stack.pop()
            sum += 1

print(sum)
