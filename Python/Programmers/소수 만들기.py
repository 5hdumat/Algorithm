# https://programmers.co.kr/learn/courses/30/lessons/12977
import math

sequence = []
cnt = 0

def dfs(depth, idx, nums, visited):
    if depth == 3:
        if is_prime_number(sum(sequence)):
            global cnt 
            cnt += 1
        return
    
    for i in range(idx, len(nums)):
        if not visited[i]:
            visited[i] = True
            sequence.append(nums[i])
            
            dfs(depth + 1, i, nums, visited)
            visited[i] = False
            
            sequence.pop()    
    
def is_prime_number(n):
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True
            
def solution(nums):
    visited = [False for _ in range(len(nums))]
    
    prime_number = is_prime_number(sum(nums))
    
    dfs(0, 0, nums, visited)
    
    return cnt
               
solution([1,2,7,6,4])
