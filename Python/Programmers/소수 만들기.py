import math 

output = []
cnt = 0

def dfs(depth, idx, visited, nums):
    if depth == 3:
        if is_prime_number(sum(output)):
            global cnt 
            cnt += 1
        return
    
    for i in range(idx, len(nums)):
        if not visited[i]:
            visited[i] = True
            output.append(nums[i])
            
            dfs(depth + 1, i, visited, nums)
            
            visited[i] = False
            output.pop()
            
def is_prime_number(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(nums):
    visited = [False for _ in range(len(nums))]
    
    dfs(0, 0, visited, nums)
    
    print(cnt)
    
solution([1,3,4,5,2,7,6,4])