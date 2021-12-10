'''
3 입력 가정
'''


def dfs(x):
    if x > 0:
        # 여기에 print를 두면 3 2 1 출력
        print(x, end='')

        dfs(x - 1)

        # Q) 여기에 print를 두면 1 2 3 출력 why?
        # A) 재귀함수와 stack을 이해하자. 참고: https://www.inflearn.com/course/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%AC%B8%EC%A0%9C%ED%92%80%EC%9D%B4-%EC%BD%94%EB%94%A9%ED%85%8C%EC%8A%A4%ED%8A%B8/lecture/42764?tab=note&speed=1
        print(x, end='')


if __name__ == "__main__":
    n = int(input())
    dfs(n)
