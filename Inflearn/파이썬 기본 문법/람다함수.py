'''
람다 함수
(다른말로는 이름이 없어 익명의 함수라고도 하고, 표현식이라고도 한다.)
'''


# 람다 안쓰고 함수로 호출
def plus_one(x):
    return x + 1


print(plus_one(1))  # 2

# 람다 사용 예제
# ! 람다는 호출하려면 변수에 할당을 해야 한다.
plus_one = lambda x: x + 1
print(plus_one(1))  # 2

'''
람다는 이럴때 유용해요!

map() 이란? 
map(함수명, 값) a라는 리스트에 plus_one 함수를 적용
'''


# 함수 표현식
def plus_one(x):
    return x + 1


a = [1, 2, 3]

print(list(map(plus_one, a)))  # [2, 3, 4]

# 람다 표현식
# 람다를 사용하면 간단히 표현 가능 (선언부터 출력까지 한줄로 가능)
print(list(map(lambda x: x + 1, a)))  # [2, 3, 4]
