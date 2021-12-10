'''
5
3
6
0
5
0
2
4
0
-1
'''
import heapq as hq

a = []

while True:
    n = int(input())

    if n == -1:  # -1이 입력되면 프로그램 종료한다.
        break

    if n == 0:  # 숫자 0 이 입력되면 최소힙에서 최솟값을 꺼내어 출력한다.
        if len(a) == 0:
            print(-1)  # 출력할 자료가 없으면 -1를 출력한다.
        else:
            print(hq.heappop(a))
    else:
        hq.heappush(a, n)