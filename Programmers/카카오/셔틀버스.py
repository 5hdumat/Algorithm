# 셔틀은 09:00 부터 n회 t분 간격으로 최대 m명을 태울 수 있다.
from collections import deque


def solution(n, t, m, timetable):
    answer = 0

    timetable = [
        int(x[:2]) * 60 + int(x[3:])
        for x in timetable
    ]

    timetable.sort()
    timetable = deque(timetable)

    # 09:00 부터 운행
    current = 540
    for _ in range(n):
        for _ in range(m):
            if timetable and timetable[0] <= current:
                answer = timetable.popleft() - 1
            else:
                answer = current

        current += t

    m = divmod(answer, 60)

    # print(str(m[0]).zfill(2) + ':' + str(m[1]).zfill(2))
    return str(m[0]).zfill(2) + ':' + str(m[1]).zfill(2)


solution(1, 1, 5,
         ["08:00", "08:01", "08:02", "08:03"])

solution(2, 1, 2,
         ["09:00", "09:00", "09:00", "09:00"])

solution(10, 60, 45,
         ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
          "23:59", "23:59", "23:59", "23:59"])
