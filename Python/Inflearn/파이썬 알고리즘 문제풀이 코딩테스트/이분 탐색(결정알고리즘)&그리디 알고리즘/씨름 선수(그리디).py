'''
5
172 67
183 65
180 70
170 72
181 60
'''
# 내 문제풀이
n = int(input())
player = []

for _ in range(n):
    h, w = map(int, input().split())
    player.append((h, w))

player.sort(key=lambda x: x[1], reverse=True)

cnt = 0
tmp_h = 0
tmp_w = 0
for h, w in player:
    if (tmp_h < h and tmp_w < w) or (tmp_h < h or tmp_w < w):
        cnt += 1
        tmp_h = h
        tmp_w = w

print(cnt)

# 강의 문제풀이
n = int(input())
body = []

for i in range(n):
    a, b = map(int, input().split())
    body.append((a, b))

body.sort(reverse=True)  # 첫번째 요소로 내림차순 정렬

cnt = 0
largest = 0
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1

print(cnt)