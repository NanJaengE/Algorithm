import sys
sys.stdin = open('input.txt', 'r')


def dfs():
    if N == M:
        for i in range(1, N+1):
            res.append(i)
        print(' '.join(map(str, res)))
        return

    if len(res) == M:
        print(' '.join(map(str, res)))
        return

    for i in range(1, N+1):
        if i not in res:
            if len(res) > 0 and res[-1] < i:
                res.append(i)
                dfs()
                res.pop()
            else:
                res.append(i)
                dfs()
                res.pop()



T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    res = []
    dfs()