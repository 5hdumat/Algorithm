# https://www.acmicpc.net/problem/2108
import sys

n = int(sys.stdin.readline()) # input() 느리니 쓰지말자..

number_list = []

for _ in range(n):
    number_list.append(int(sys.stdin.readline()))

# 산술 평균
print(round(sum(number_list) / n))

# 중앙 값
number_list.sort()
print(number_list[n//2])
      
# # 최빈값 (시간초과 남)
# dup_list = list(set(number_list)) # 중복제거
# mode_list = []
# max_cnt = 0
# for i in dup_list:
#     if max_cnt == number_list.count(i):
#         mode_list.append(i)
#     elif max_cnt < number_list.count(i):
#         mode_list = []
#         mode_list.append(i)
#         max_cnt = number_list.count(i)
        
# if len(mode_list) >= 2:    
#     mode_list.sort()
#     print(mode_list[1])
# else:
#     print(mode_list[0])
    
# 최빈값 외장함수 사용
from collections import Counter

mode = Counter(number_list).most_common()

if len(mode) > 1: 
    if mode[0][1] == mode[1][1]:
        print(mode[1][0])
    else:
        print(mode[0][0])
else:
    print(mode[0][0])
    
# 범위
print(max(number_list) - min(number_list))
