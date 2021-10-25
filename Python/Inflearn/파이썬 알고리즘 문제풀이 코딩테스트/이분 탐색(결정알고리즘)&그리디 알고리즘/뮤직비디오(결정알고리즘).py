'''
9 3
1 2 3 4 5 6 7 8 9
'''

# 용량을 받아서 DVD 몇장을 만들 수 있는지 체크
# 만들 수 있는 DVD가 m값 보다 작으면 용량이 큰 것
def Count(capacity):
    cnt = 1 # 최소 1장
    sum = 0

    for x in songs:
        if sum + x > capacity:
            cnt += 1
            sum = x
        else:
            sum += x

    return cnt


n, m = map(int, input().split())
songs = list(map(int, input().split()))
max = max(songs)

lt = 1
rt = sum(songs)
res = 0
while lt <= rt:
    mid = (lt + rt) // 2

    '''
    Count에 용량을 던졌는데 만들고자 하는 DVD 갯수
    보다 적으면 rt값을 줄여야 함(용량이 너무 크니까)
    '''
    if mid >= max and Count(mid) <= m:
        res = mid
        rt = mid - 1
    else:
        lt = mid + 1

print(res)
