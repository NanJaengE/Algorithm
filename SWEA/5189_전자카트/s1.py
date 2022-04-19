import sys
sys.stdin = open('sample_input.txt', 'r')


def perm(n, k):
    if n == k:
        global mini
        total_cost = 0
        for j in range(n):
            if j == 0:
                total_cost += cost[1][p[j]]
                total_cost += cost[p[j]][p[j + 1]]
            elif j == n-1:
                total_cost += cost[p[j]][1]
            else:
                total_cost += cost[p[j]][p[j + 1]]
            if total_cost > mini:
                break
        if total_cost < mini:
            mini = total_cost
    else:
        for i in range(k, n):
            p[k], p[i] = p[i], p[k]
            perm(n, k+1)
            p[k], p[i] = p[i], p[k]


T = int(input())
for test in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]

    # 0으로 감싸주기
    for i in range(N):
        cost[i].append(0)
        cost[i].insert(0, 0)
    cost.append([0] * (N + 2))
    cost.insert(0, [0] * (N + 2))

    p = []
    mini = N*100
    for n in range(2, N+1):
        p.append(n)
    n = len(p)
    perm(n, 0)
    print(f'#{test} {mini}')

