'''
3
1 5 7
'''
def dfs(l, sum):
    if sum > s:
        return

    if l == n:
        if sum > 0:
            res.add(sum)
        return
    else:
        dfs(l + 1, sum + a[l]) # 추를 왼쪽에 둘 때
        dfs(l + 1, sum - a[l]) # 추를 오른쪽에 둘 때
        dfs(l + 1, sum) # 추를 하나도 사용하지 않을 때


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    res = set()
    tmp = []
    dfs(0, 0)
    print(s-len(res))
