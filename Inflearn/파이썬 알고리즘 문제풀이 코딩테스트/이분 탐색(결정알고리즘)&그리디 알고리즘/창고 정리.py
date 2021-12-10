'''
10
69 42 68 76 40 87 14 65 76 81
50
'''
n = int(input())
box = list(map(int, input().split()))
m = int(input())

box.sort()

for i in range(m):
    box[n - 1] -= 1
    box[0] += 1

    box.sort()

print(box[n - 1] - box[0])

# 시간초과가 난다면? 해쉬를 이용하자.
n = int(input())
box = list(map(int, input().split()))
m = int(input())

cnt = [0] * 101  # 창고 가로의 길이 조건 L(1<=L<=100)
max_h = float('-inf')
min_h = float('inf')
for x in box:
    cnt[x] += 1
    if x > max_h:
        max_h = x

    if x < min_h:
        min_h = x

for _ in range(m):
    if cnt[max_h] == 1:
        cnt[max_h] -= 1
        max_h -= 1
        cnt[max_h] += 1
    else:
        cnt[max_h] -= 1
        cnt[max_h - 1] += 1

    if cnt[min_h] == 1:
        cnt[min_h] -= 1
        min_h += 1
        cnt[min_h] += 1
    else:
        cnt[min_h] -= 1
        cnt[min_h + 1] += 1

print(max_h - min_h)
