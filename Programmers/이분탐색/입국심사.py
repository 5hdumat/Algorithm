'''
이진 탐색을 이용하여 최대 가능한 시간(최소검색시간을 가진 검색원의 검색 시간 * 사람수)과 0초를 기준으로 가능한 시간을 줄여갑니다.
각 탐색마다 middle 값의 시간동안 각 검색원들이 가능한 검색가능한 사람 수를 모두 더한 후 비교합니다. 가능하면 답으로 갱신, 가능하지 않으면 넘어가는 과정을 반복합니다.
'''
def Count(mid, times):
    cnt = 0

    for x in times:
        cnt += mid // x

    return cnt


def solution(n, times):
    answer = 0
    lt = 0
    rt = min(times) * n

    while lt <= rt:
        mid = (lt + rt) // 2
        if Count(mid, times) >= n:
            answer = mid
            rt = mid -1
        else:
            lt = mid + 1

    return answer


solution(6, [7, 10])
