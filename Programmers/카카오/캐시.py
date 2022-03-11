import collections


def solution(cacheSize, cities):
    answer = 0
    cache = collections.deque(maxlen=cacheSize)

    for city in list(map(lambda x : x.lower(), cities)):
        if cache.count(city) == 0:
            answer += 5
            cache.append(city)
        else:
            # 캐시 충돌이 발생하면 최신화
            cache.remove(city)
            cache.append(city)
            answer += 1

    print(answer)
    return answer


solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"])
solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])
solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])