'''
5
1 4
2 3
3 5
4 6
5 7
'''
# 내 문제풀이
n = int(input())
a = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    a.append(tmp)

a.sort(key=lambda x: x[1])

res = 0
end_time = -1
for i in range(0, n):
    if a[i][0] >= end_time:
        res += 1
        end_time = a[i][1]

print(res)

# 강의 문제 풀이
n = int(input())
meeting = []

for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))  # 튜플 자료형으로 기입

# 정렬하려는 키의 기준을 익명함수 lambda로 정의 (매개변수 x의 1번째를 기준으로 정렬, x의 1번째 값이 같다면 0번째로 정렬)
meeting.sort(key=lambda x: (x[1], x[0]))

et = 0
cnt = 0
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1

print(cnt)