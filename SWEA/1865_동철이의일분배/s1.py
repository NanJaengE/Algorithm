import sys
sys.stdin = open('input.txt', 'r')


def dfs(work, success_rate):
    global best

    # 곱하는 도중 확률이 이전보다 낮아지면
    if best >= success_rate:
        return

    # 마지막 업무까지 다 배정했으면 이전확률과 비교하여 더 높다면
    if work == N:
        if best < success_rate:
            best = success_rate
        return

    # 다음 업무을 배정할 직원을 고르고 인덱스를 마킹해서 중복배정을 방지
    for i in range(N):
        if idx[i] == 0:
            idx[i] = 1
            dfs(work+1, success_rate * work_chart[work][i]/100)
            idx[i] = 0


T = int(input())
for test in range(1, T+1):
    N = int(input())
    idx = [0]*N
    work_chart = [list(map(int, input().split())) for _ in range(N)]
    # 기본 최소확률을 0으로 잡기
    best = 0

    dfs(0, 1)
    print(f'#{test} {best*100:6f}')