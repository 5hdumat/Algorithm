# https://www.acmicpc.net/problem/2504

# 비효율적인 재귀 연산으로 인한 시간초과 발생
# https://www.acmicpc.net/problem/2504

# 비효율적인 재귀 연산으로 인한 시간초과 발생
import sys

# (()[[]])([]) 입력 가정
brackets = list(sys.stdin.readline().strip())

if len(brackets) % 2 != 0:
    print(0)
    exit()

stack = []
for bracket in brackets:
    if bracket in ['(', '[']: # ((
        stack.append(bracket)
        
    elif bracket == ')': 
        cnt = 0
        
        while len(stack) != 0:
            item = stack.pop() # stack => ['(', '('] -> '(', ['(', 2] -> 2
            
            if item == '(':
                if cnt == 0:
                    stack.append(2) # stack => ['(', 2]
                else:
                    stack.append(2 * cnt)
                break
            
            elif item == '[':
                print(0)
                exit()
        
            else:
                cnt += int(item) # 3
            
    elif bracket == ']': 
        cnt = 0
        
        while len(stack) != 0:
            item = stack.pop() # stack => ['(', '('] -> '(', ['(', 2] -> 2
            
            if item == '[':
                if cnt == 0:
                    stack.append(3) # stack => ['(', 2]
                else:
                    stack.append(3 * cnt)
                break
            
            elif item == '(':
                print(0)
                exit()
        
            else:
                cnt += int(item) # 3
            
for i in stack:
    if i in ['(', '[']:
        print(0)
    else:
        print(sum(stack))
    
    exit()

import sys

# (()[[]])([]) 입력 가정
brackets = list(sys.stdin.readline().strip())

stack = []
for bracket in brackets:
    if bracket in ['(', '[']: # ((
        stack.append(bracket)
        
    elif bracket == ')': 
        cnt = 0
        
        while len(stack) != 0:
            item = stack.pop() # stack => ['(', '('] -> '(', ['(', 2] -> 2
            
            if item == '(':
                if cnt == 0:
                    stack.append(2) # stack => ['(', 2]
                else:
                    stack.append(2 * cnt)
                break
            
            elif item == '[':
                print(0)
                exit()
        
            else:
                cnt += int(item) # 3
            
    elif bracket == ']': 
        cnt = 0
        
        while len(stack) != 0:
            item = stack.pop() # stack => ['(', '('] -> '(', ['(', 2] -> 2
            
            if item == '[':
                if cnt == 0:
                    stack.append(3) # stack => ['(', 2]
                else:
                    stack.append(3 * cnt)
                break
            
            elif item == '(':
                print(0)
                exit()
        
            else:
                cnt += int(item) # 3

output = 0        
for i in stack:
    if i in ['(', '[']:
        print(0)
        exit()
    else:
        output += i

print(output)
    
    
