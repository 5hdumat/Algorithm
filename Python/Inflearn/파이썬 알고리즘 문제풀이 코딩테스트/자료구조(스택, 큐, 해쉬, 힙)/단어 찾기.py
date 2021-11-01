'''
5
big
good
sky
blue
mouse
sky
good
mouse
big
'''
n = int(input())
need = {}
sum = 0
for _ in range(n):
    word = input()
    need[hash(word)] = word
    sum += hash(word)

for _ in range(n - 1):
    sum -= hash(input())

print(need[sum])

# 강의 문제 풀이
n = int(input())
p = dict()

for i in range(n):
    word = input()
    p[word] = 1

for i in range(n - 1):
    word = input()
    p[word] = 0

for key, value in p.items():
    if value == 1:
        print(key)
