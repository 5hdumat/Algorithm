from collections import deque

max = 10000  # 직선의 좌표 점은 1부터 10,000 까지이다.
ch = [0] * (max + 1)
dis = [0] * (max + 1)

s, e = map(int, input().split())
ch[s] = 1
dis[s] = 0

dq = deque()  # 큐 생성
dq.append(s)

cnt = 1
while dq:
    now = dq.popleft()


    for next in (now - 1, now + 1, now + 5):
        if 0 < next <= max:
            if ch[next] == 0:
                dq.append(next)

                ch[next] = 1
                dis[next] = dis[now] + 1

        if next == e:
            dq.clear()
            print(dis[next])
            break

