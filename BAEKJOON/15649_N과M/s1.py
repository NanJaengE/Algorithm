import sys
sys.stdin = open('input.txt', 'r')


def dfs():

    if len(res) == M:
        print(' '.join(map(str, res)))
        return

    for i in range(1, N+1):
        if i not in res:
            res.append(i)
            dfs()
            res.pop()


T = int(input())
for test in range(T):
    N, M = map(int, input().split())
    res = []
    dfs()
