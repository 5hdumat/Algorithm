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

heap = []

# 파이썬의 heapq는 최소힙으로만 동작하기 때문에
# 최대힙으로 사용하려면 약간의 응용이 필요하다.
# 본인의 경우 최대값에 -를 붙여 숫자가 클수록 최솟값으로 동작하게 하였다.
while True:
    n = int(input())

    if n == -1:
        break

    if n == 0:
        if len(heap) == 0:
            print(-1)
        else:
            print(-hq.heappop(heap))  # 출력할땐 - 붙여서 제거한다
    else:
        hq.heappush(heap, -n)
